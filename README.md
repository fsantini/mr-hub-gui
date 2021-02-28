# mr-hub-gui

A Python GUI to add packages to MR-Hub.

This tool generates the required JSON description for MR-Hub, and then helps in creating the forked Github repository.

## Requirements

This tool is written in Python. Version 3.6 or more are required.

In addition to Python, you will also need:
- A Github account.
- Git installed on your system, and in the path.
- Git properly configured (with global user.name and user.email variables set).

## Installation

You can install this program directly from pip:

`pip install mr-hub-gui`

and subsequently you can directly launch `mr-hub-gui`

Alternatively, you can clone the github repository and launch the `mr-hub-gui` script directly, or install it from the
local clone with `pip install -e .` .

The following python libraries are required: `PyGithub`, `PySide2`, `requests`.

## Usage

Launch the `mr-hub-gui` program. Fill in all the required fields.
You can load and save your settings as JSON (which you can also then use to manually create the repository and the pull
request, if you wish).

Once you are ready, you can select Prepare MR-Hub submission from the File menu. This will fork the main MR-Hub repo
inside Github, create a local copy, and modify it. Finally, the pull request page will be open in your browser. 
Review it and approve it.

See the [MR hub github page](https://github.com/ISMRM/mrhub) for more information.

## Compatibility

This program was tested with Linux and Windows.