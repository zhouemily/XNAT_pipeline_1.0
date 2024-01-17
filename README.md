# XNAT Pipeline 1.0

## Overview

The XNAT Pipeline 1.0 is a versatile toolkit for automating data processing and analysis workflows on neuroimaging data stored on an XNAT server. It provides a set of Python scripts and utilities to streamline the execution of data pipelines, making it easier for researchers and data analysts to work with their neuroimaging data efficiently.

## Features

- Automate data processing and analysis workflows.
- Execute specific pipelines for preprocessing, analysis, and more.
- Seamless integration with XNAT servers.
- Configuration options for input data, output paths, and processing settings.
- Designed for researchers working with neuroimaging data.

## Prerequisites

Before using the XNAT Pipeline 1.0, ensure that you have the following prerequisites installed:

- Python 3.x
- Required Python packages listed in the script files
- XNAT account credentials with appropriate permissions

## Usage

    Clone this repository to your local machine using Git:
        git clone https://github.com/zhouemily/XNAT_pipeline_1.0.git
        pip install -r requirements.txt (to install required python modules)

##############################################################################
Install python and set prefered python environment:

"pyenv" is a popular tool for managing Python versions on your system. It allows you to install and switch between different Python versions with ease. Here are the basic steps to use "pyenv":
    Manual Installation:
    You can follow the instructions on the GitHub repository: 
        https://github.com/pyenv/pyenv

    Add pyenv to Your Shell:
    To enable pyenv, you need to add it to your shell configuration file 
    (e.g., .bashrc, .zshrc, or .profile). Add the following line at the 
    end of the appropriate file:
        eval "$(pyenv init -)"

    For example, if you're using Bash, add it to your ~/.bashrc 
    or ~/.bash_profile file.
  
    After adding the above line to your shell configuration file, 
    restart your shell or run the following command to apply the changes:
        exec "$SHELL"

    Install Python Versions:
    You can install Python versions using pyenv. For example, to install 
    Python 3.11.6, you can use the following command:
        pyenv install 3.11.6

To create and manage virtual environments, Python developers often use tools like virtualenv or venv (which is included in Python 3). Additionally, third-party tools like pyenv-virtualenv can be used in combination with pyenv to manage virtual environments and Python versions effectively.
Here are some terminal command and output examples:
        python3 -m venv myenv_3.11.6_py (venv came with python 3.3 or later, prefered)
        source myenv_3.11.6_py/bin/activate
            or
        pyenv virtualenv 3.11.6 myenv_3.11.6_py (need to install virtualenv first if not exist)

    (to activate you pyenv environment: myenv_3.11.6.py)
        pyenv activate myenv_3.11.6_py 
            or 
     run the following source command directly in myenv_3.11.6 directory:
    (base) bash-5.1$ source ~/.pyenv/versions/myenv_3.11.6_py/bin/activate
    (myenv_3.11.6_py) (base) bash-5.1$ 


Now your pyenv special environment is established, you can intall other needed python libs with
pip or pi3 (prefered if python3 is used like python 3.11.6)

    (myenv_3.11.6_py) (base) bash-5.1$ pip install --upgrade pip
    Requirement already satisfied: 
        pip in /Users/zhou/.pyenv/versions/3.11.6/envs/myenv_3.11.6_py/lib/python3.11/site-packages (23.2.1)
    Collecting pip
        Obtaining dependency information for pip from https://files.pythonhosted.org/packages/15/aa/3f4c7bcee2057a76562a5b33ecbd199be08cdb4443a02e26bd2c3cf6fc39/pip-23.3.2-py3-none-any.whl.metadata
    Using cached pip-23.3.2-py3-none-any.whl.metadata (3.5 kB)
    Using cached pip-23.3.2-py3-none-any.whl (2.1 MB)
    Installing collected packages: pip
    Attempting uninstall: pip
        Found existing installation: pip 23.2.1
        Uninstalling pip-23.2.1:
        Successfully uninstalled pip-23.2.1
        Successfully installed pip-23.3.2
(myenv_3.11.6_py) (base) bash-5.1$ 

    if you downloaded  XNAT_pipeline_1.0 zip file from Github at:
        https://github.com/zhouemily/XNAT_pipeline_1.0

    you can unzip the files  and cd to the directory of your choices:
    for exmaple:
    (myenv_3.11.6_py) (base) bash-5.1$ cd ~/xnat/xnat1.0
    (myenv_3.11.6_py) (base) bash-5.1$ pwd
        /Users/zhou/xnat/xnat1.0
    (myenv_3.11.6_py) (base) bash-5.1$ 
    (myenv_3.11.6_py) (base) bash-5.1$ ls *py; ls *sh
         XNAT_file_pipeline.py	run.py			test_dcm.py		xnat_send.py
         run.sh			run_test.sh		run_xnat_pipeline.sh	weasis.sh
    (myenv_3.11.6_py) (base) bash-5.1$ 

    (See more detailed information on readme_run.py on how to run scripts)

For single file processing:
(myenv_3.11.6_py) (base) bash-5.1$ ./XNAT_file_pipeline.py -h
Program Started
DEBUG [main:434]: This is a debug message from debug_print function
2024-01-16 15:0016 cups id is needed:

example: ./Xnat_file_pipeline.py -id CUPS003


            Usage: ./XNAT_file_pipeline.py -id cups_id [-h] [-D] [-v] [-fpng png_fname] [-fsvg1 svg_fname1] [-fsvg2 svg_fname2]
            -h			print help menu
            -id [cups_id]       input cups_id
            -D                  run debug mode
            -v                  enable verbose
            -d                  input root path directory
            
(myenv_3.11.6_py) (base) bash-5.1$ 

For many file in specified direcory:
(myenv_3.11.6_py) (base) bash-5.1$ ./run.py -i CUPS.log
need input file: usage: ./run.py -i CUPS.log
Directory './dcm_dir' already exists.
2024-01-16 15:0258 excute command::OK: ./XNAT_file_pipeline.py -L -id CUPS003
......


Test all new dcm files created at ./dcm_dir:
./test_dcm.sh

or 
use Weasis to analyze the new dcm files.

After you are sure those dcm file are well tested, you can upload those dcm files automatically to
the XNAT server.
    prerequirment:
##use xnatpy and netrc modules
#creat ~/.netrc to store "machine", user, and passwd for security purpose
##use encrytion (Not plain passwd) to be safer if needed
#for example: vi ~/.netrc, you will see:
#############################################################
#machine    xnat1.beckman.illinois.edu
#login      "loginname"
#password   "xxxxxxxxx"
##############################################################
#IMPORTANT:
#after create the ~/.netrc file, you need set the correct permission:
#chmod 600 ~/.netrc
#This command sets the permissions of the ~/.netrc file to allow 
#read and write access only to the owner (you) and restricts access to everyone else.
################################################################

Finaly if you want to deactivate your pyenv, simply type at the prompt:
...
(myenv_3.11.6_py) (base) bash-5.1$pwd 
/Users/zhou/xnat/xnat1.0
(myenv_3.11.6_py) (base) bash-5.1$ ls
XNAT_pipeline_1.0-main
(myenv_3.11.6_py) (base) bash-5.1$ deactivate
(base) bash-5.1$ 
deactivate
