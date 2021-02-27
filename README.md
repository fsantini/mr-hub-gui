# mr-hub-gui
A Python GUI to add packages to MR-Hub.

This tool generates the required JSON description for MR-Hub, and then helps in creating the forked Github repository.

## Requirements

This tool is written in Python. Version 3.6 or more are required.

In addition to Python, you will also require:
- A Github account.
- Git installed on your system, and in the path.
- Git properly configured (with global user.name and user.email variables set).

## Usage

Launch the `mr-hub-gui` program. Fill in all the required fields.
You can load and save your settings as JSON (which you can also then use to manually create the repository and the pull
request, if you wish).

Once you are ready, you can select Prepare MR-Hub submission from the File menu. This will fork the main MR-Hub repo
inside Github, create a local copy, and modify it. Finally, the pull request page will be open in your browser. 
Review it and approve it.

See the [MR hub github page](https://github.com/ISMRM/mrhub) for more information.
