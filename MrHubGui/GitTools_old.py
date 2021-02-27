from github import Github
import subprocess
import os
import shutil
import json

BASE_REPO_NAME = 'ismrm/mrhub'
MAIN_BRANCH = 'master'

settings = {
    'LOCAL_DIR': 'local_mrhub_repo',
    'USER': '__token__',
    'PASS': '',
    'FORKED_REPO': None
}


class GitError(Exception):
    pass

def github_repo_url(github_repo_obj, use_auth=False):
    return f'https://github.com/{github_repo_obj.full_name}.git'


def get_github_compare_url():
    if settings['FORKED_REPO'] is None:
        raise GitError('Repository not forked')
    return f"https://github.com/{settings['FORKED_REPO'].full_name}/compare/{get_branch_name()}"


def create_askpass_posix():
    askpass_file = os.path.join(settings['LOCAL_DIR'], 'askpass.sh')
    with open(askpass_file, 'w') as f:
        f.write(
f"""#!/bin/sh
if echo $1 | grep -q Username
then
    echo {settings['USER']}
fi
if echo $1 | grep -q Password
then
    echo {settings['PASS']}
fi  
""")
    os.chmod(askpass_file, 0o777)
    return os.path.abspath(askpass_file)

def create_askpass_win():
    askpass_file = os.path.join(settings['LOCAL_DIR'], 'askpass.bat')
    with open(askpass_file, 'w') as f:
        f.write(
f"""@set arg=%%~1
@if (%%arg:~0,8%%)==(Username) echo {settings['USER']}
@if (%%arg:~0,8%%)==(Password) echo {settings['PASS']}
""")
    return os.path.abspath(askpass_file)


def create_askpass_file():
    if os.name == 'posix':
        return create_askpass_posix()
    elif os.name == 'nt':
        return create_askpass_win()
    else:
        raise GitError('OS not supported')


def user_pass_to_bytes():
    return (settings['USER'] + '\n' + settings['PASS'] + '\n').encode()


def git(git_options, working_dir=None, send_auth=False):
    original_dir = os.getcwd()
    if working_dir:
        os.chdir(working_dir)

    if send_auth:
        askpass_file = create_askpass_file()
        os.environ['GIT_ASKPASS'] = askpass_file

    print('git ' + git_options)
    proc = subprocess.run('git ' + git_options, capture_output=True, shell=True)
    print('Stdout')
    print(proc.stdout)
    print('Stderr')
    print(proc.stderr)

    if send_auth:
        os.remove(askpass_file)

    if working_dir:
        os.chdir(original_dir)
    return proc.returncode, proc.stdout.decode(), proc.stderr.decode()


def check_git_settings():
    ret, out, err = git('config --get user.name')
    if ret or not out: return False
    ret, out, err = git('config --get user.email')
    if ret or not out: return False
    return True


def initialize_github(credentials, new_branch_name, local_dir = None):
    if local_dir:
        settings['LOCAL_DIR'] = local_dir

    if isinstance(credentials, tuple):
        github = Github(*credentials)
        settings['USER'] = credentials[0]
        settings['PASS'] = credentials[1]
    else:
        github = Github(credentials)
        settings['PASS'] = credentials

    # get authenticated user
    github_user = github.get_user()

    # get a reference to the base repo
    base_repo = github.get_repo(BASE_REPO_NAME)

    # make a fork
    forked_repo = github_user.create_fork(base_repo)

    return_code, out, err = git(f'clone {github_repo_url(forked_repo)} "{settings["LOCAL_DIR"]}"')
    if return_code:
        if 'already exists' in err:
            print('Warning: repo already exists')
        else:
            raise GitError('Error during cloning')

    settings['FORKED_REPO'] = forked_repo

    git(f'checkout {MAIN_BRANCH}', settings['LOCAL_DIR'])
    git(f'remote add upstream {github_repo_url(base_repo)}', settings['LOCAL_DIR'])
    git('pull', settings['LOCAL_DIR'])
    git('fetch upstream', settings['LOCAL_DIR'])
    git(f'merge -s recursive -Xtheirs upstream/{MAIN_BRANCH}', settings['LOCAL_DIR'])
    ret, out, err = git(f'checkout -b "{new_branch_name}"', settings['LOCAL_DIR'])
    if 'fatal' in err.lower():
        raise GitError('Branch already exists')


def copy_image(image_file, image_name):
    repo_dir = os.path.abspath(settings['LOCAL_DIR'])
    shutil.copy(image_file, os.path.join(repo_dir, 'images_packages', image_name))
    git(f'add {os.path.join("images_packages", image_name)}', settings['LOCAL_DIR'])


def add_package(package_dict):
    original_dir = os.getcwd()
    os.chdir(settings['LOCAL_DIR'])
    current_package_lines = open(os.path.join('_data', 'projects.json'), 'r').readlines()
    # find opening [
    bracket_line = -1
    for number, line in enumerate(current_package_lines):
        if line.strip() == '[':
            bracket_line = number
            break

    assert bracket_line > -1, "Malformed project.json file"
    package_json = json.dumps(package_dict, indent=2) + ','
    #insert lines in inverse order
    for line in package_json.splitlines()[::-1]:
        current_package_lines.insert(bracket_line+1, ' '*2 + line + '\n')

    with open(os.path.join('_data', 'projects.json'), 'w') as f:
        f.writelines(current_package_lines)

    git('commit -a -m "Package addition - generated by mr-hub-gui"')

    git(f'push -u origin {get_branch_name()}', send_auth=True)

    os.chdir(original_dir)


def get_branch_name():
    ret, out, err = git('status', settings['LOCAL_DIR'])
    for line in out.splitlines():
        if line.lower().startswith('on branch '):
            return line[len('on branch '):]
    return None


def delete_local_repository():
    shutil.rmtree(settings['LOCAL_DIR'])