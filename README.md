# IE Bank backend

- [IE Bank backend](#ie-bank-backend)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Recommended tutorials](#recommended-tutorials)
  - [Configure your local environment](#configure-your-local-environment)
    - [Install Prerequisites](#install-prerequisites)
    - [Set up your local environment with VSCode](#set-up-your-local-environment-with-vscode)
  - [Run and debug the backend locally](#run-and-debug-the-backend-locally)


## Overview

This is the repository for the backend code of the IE Bank web app

![IE Bank app logical view](images/ie-bank-app.png)

## Requirements

This source code works under the following technologies:
- [Python 3.11.5](https://www.python.org/downloads/release/python-3115/)
- [Flask 2.2.2](https://pypi.org/project/Flask/2.2.2/)
- [Flask-Cors 3.0.10](https://pypi.org/project/Flask-Cors/3.0.10/)
- [Flask-SQLAlchemy 2.5.1](https://pypi.org/project/Flask-SQLAlchemy/2.5.1/)
- [psycopg2 2.9.7](https://pypi.org/project/psycopg2/)
- [python-dotenv 0.21.0](https://pypi.org/project/python-dotenv/0.21.0/)
- [SQLAlchemy 1.4.41](https://pypi.org/project/SQLAlchemy/1.4.41/)
- [SQL Lite 3.43.0](https://www.sqlite.org/download.html)

## Recommended tutorials
- [Flask](https://flask.palletsprojects.com/en/2.3.x/tutorial/)
- [Flask on VS Code](https://code.visualstudio.com/docs/python/tutorial-flask)
- Linkedin Learning: [Building RESTful APIs with Flask](https://www.linkedin.com/learning/building-restful-apis-with-flask/)
- [SQLite](https://www.sqlitetutorial.net/)

## Configure your local environment

### Install Prerequisites

- **Install git**. Install git from [here](https://git-scm.com/downloads).
- **Install Python**. Install Python 3.11.5 from [here](https://www.python.org/downloads/release/python-3115/). Make sure to select the option to add Python to your PATH while installing.
- **Install VSCode**. Install VSCode from [here](https://code.visualstudio.com/download).
- **Install Python VSCode extension**. Install the Python extension for VSCode from [here](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
- **Install SQL Lite**. Install SQL Lite from [here](https://www.sqlite.org/download.html). SQLite provides various tools for working across platforms e.g., Windows, Linux, and Mac. You need to select an appropriate version to download. After downloading:
  - On Windows, unzip the downloaded file into a directory (e.g., `C:\sqlite`). Add the `C:\sqlite` directory to your PATH environment variable.
  - On Linux, open a terminal and run the command `sudo apt-get install sqlite3`.
  - On MacOS, open a terminal and run the command `brew install sqlite3`.

### Set up your local environment with VSCode

1. **Create the virtual environment**. In VS Code, open the Command Palette (`View` > `Command Palette` or [`Ctrl`+`Shift`+`P`]). Then select the `Python: Create Environment` command to create a virtual environment in your workspace. Select `venv` and then the Python environment you want to use to create it.

![Python - Create Environment on VSCode](https://code.visualstudio.com/assets/docs/python/flask-tutorial/command-palette.png)

2. **Activate your virtual environment**. After your virtual environment creation has been completed, run [Terminal: Create New Terminal](https://code.visualstudio.com/docs/terminal/basics) \[`Ctrl`+`Shift`+ `` ` ``]) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script
3. **Install Flask in the virtual environment**. In the VS Code Terminal, run the following command:

You now have a self-contained environment ready for writing Flask code. VS Code activates the environment automatically when you use Terminal: Create New Terminal.

```bash
$ python -m pip install flask
```

## Run and debug the backend locally

1. **Debug the app locally**. In VS Code, switch to the `Run and Debug` view (using the left-side activity bar or `Ctrl` + `Shift` + `D`). You may see the message "To customize Run and Debug create a launch.json file". VS Code can create that for you if you click on the create a launch.json file link:

![VS Code create launch file](https://code.visualstudio.com/assets/docs/python/shared/debug-panel-initial-view.png)

2. **Set and run debug configuration for `Flask`**. Select the link and VS Code will prompt for a debug configuration. Select `Flask` from the dropdown and VS Code will populate a new `launch.json` file in the `.vscode` folder with a Flask run configuration. The `launch.json` file contains a number of debugging configurations, each of which is a separate JSON object within the configuration array. Edit the `.vscode/launch.json` configuration file with the snippet below and save (`Ctrl`+`S`). In the debug configuration dropdown list select the `Python: Flask configuration`.

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_DEBUG": "1",
                "ENV": "local",
                "DBUSER":"",
                "DBPASS":"",
                "DBHOST":"",
                "DBNAME":""
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```