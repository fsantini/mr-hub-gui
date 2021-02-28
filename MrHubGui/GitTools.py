from github import Github
from github.GithubException import BadCredentialsException
import subprocess
import os
import shutil
import json

BASE_REPO_NAME = 'ismrm/mrhub'
MAIN_BRANCH = 'master'

DEFAULT_LOCAL_DIR = 'local_mrhub_repo'

settings = {
    'LOCAL_DIR': 'local_mrhub_repo',
    'USER': '__token__',
    'PASS': '',
    'FORKED_REPO': None
}


class GitError(Exception):
    pass

class GitTools:

    def __init__(self, credentials, new_branch_name, local_dir = DEFAULT_LOCAL_DIR):
        if isinstance(credentials, tuple):
            self.github = Github(*credentials)
            self.user = credentials[0]
            self.password = credentials[1]
        else:
            self.github = Github(credentials)
            self.user = '__token__'
            self.password = credentials

        self.local_dir = os.path.abspath(local_dir)
        self.new_branch_name = new_branch_name
        self.forked_repo = None

    def initialize_github(self):
        # get authenticated user
        github_user = self.github.get_user()

        try:
            print(github_user.name)
        except BadCredentialsException:
            raise GitError('Authentication failed')

        # get a reference to the base repo
        base_repo = self.github.get_repo(BASE_REPO_NAME)

        # make a fork
        self.forked_repo = github_user.create_fork(base_repo)

        return_code, out, err = self.git(f'clone {self.github_repo_url()} "{self.local_dir}"')
        if return_code:
            if 'already exists' in err:
                print('Warning: repo already exists')
            else:
                raise GitError('Error during cloning')

        self.git(f'checkout {MAIN_BRANCH}', self.local_dir)
        self.git(f'remote add upstream {self.github_repo_url(base_repo)}', self.local_dir)
        self.git('pull', self.local_dir)
        self.git('fetch upstream', self.local_dir)
        self.git(f'merge -s recursive -Xtheirs upstream/{MAIN_BRANCH}', self.local_dir)
        ret, out, err = self.git(f'checkout -b "{self.new_branch_name}"', self.local_dir)
        if 'fatal' in err.lower():
            raise GitError('Branch already exists')

    def github_repo_url(self, repo=None):
        if repo is None:
            repo = self.forked_repo
        return f'https://github.com/{repo.full_name}.git'

    def github_compare_url(self):
        if self.forked_repo is None:
            raise GitError('Repository not forked')
        return f"https://github.com/{self.forked_repo.full_name}/compare/{self.get_branch_name()}"

    def create_askpass_posix(self):
        askpass_file = os.path.join(self.local_dir, 'askpass.sh')
        with open(askpass_file, 'w') as f:
            f.write(
f"""#!/bin/sh
if echo $1 | grep -q Username
then
    echo {self.user}
fi
if echo $1 | grep -q Password
then
    echo {self.password}
fi  
""")
        os.chmod(askpass_file, 0o777)
        return os.path.abspath(askpass_file)

    def create_askpass_win(self):
        askpass_file = os.path.join(self.local_dir, 'askpass.bat')
        with open(askpass_file, 'w') as f:
            f.write(
f"""@set arg=%%~1
@if (%%arg:~0,8%%)==(Username) echo {self.user}
@if (%%arg:~0,8%%)==(Password) echo {self.password}
""")
        return os.path.abspath(askpass_file)

    def create_askpass_file(self):
        if os.name == 'posix':
            return self.create_askpass_posix()
        elif os.name == 'nt':
            return self.create_askpass_win()
        else:
            raise GitError('OS not supported')

    @staticmethod
    def git_command(git_options, working_dir=None):
        cmd = 'git '
        if working_dir:
            cmd += f'-C "{working_dir}" '

        print(cmd + git_options)
        proc = subprocess.run(cmd + git_options, capture_output=True, shell=True)
        print('Stdout')
        print(proc.stdout)
        print('Stderr')
        print(proc.stderr)

        return proc.returncode, proc.stdout.decode(), proc.stderr.decode()

    def git(self, git_options, working_dir=None, send_auth=False):
        if send_auth:
            askpass_file = self.create_askpass_file()
            os.environ['GIT_ASKPASS'] = askpass_file

        ret, out, err = GitTools.git_command(git_options, working_dir)

        if send_auth:
            os.remove(askpass_file)
            del os.environ['GIT_ASKPASS']

        return ret, out, err

    @staticmethod
    def check_git_settings():
        ret, out, err = GitTools.git_command('config --get user.name')
        if ret or not out: return False
        ret, out, err = GitTools.git_command('config --get user.email')
        if ret or not out: return False
        return True

    def copy_image(self, image_file, image_name):
        repo_dir = os.path.abspath(self.local_dir)
        shutil.copy(image_file, os.path.join(repo_dir, 'images_packages', image_name))
        self.git(f'add {os.path.join("images_packages", image_name)}', self.local_dir)

    def add_package(self, package_dict):
        original_dir = os.getcwd()
        os.chdir(self.local_dir)
        current_package_lines = open(os.path.join('_data', 'projects.json'), 'r', encoding='utf-8').readlines()
        # find opening [
        bracket_line = -1
        for number, line in enumerate(current_package_lines):
            if line.strip() == '[':
                bracket_line = number
                break

        assert bracket_line > -1, "Malformed project.json file"
        package_json = json.dumps(package_dict, indent=2) + ','
        # insert lines in inverse order
        for line in package_json.splitlines()[::-1]:
            current_package_lines.insert(bracket_line + 1, ' ' * 2 + line + '\n')

        with open(os.path.join('_data', 'projects.json'), 'w', encoding='utf-8') as f:
            f.writelines(current_package_lines)

        self.git('commit -a -m "Package addition - generated by mr-hub-gui"', working_dir=self.local_dir)

        self.git(f'push -u origin {self.get_branch_name()}', working_dir=self.local_dir, send_auth=True)

        os.chdir(original_dir)

    def get_branch_name(self):
        ret, out, err = self.git('status', self.local_dir)
        for line in out.splitlines():
            if line.lower().startswith('on branch '):
                return line[len('on branch '):]
        return None

    def delete_local_repository(self):
        shutil.rmtree(self.local_dir)
