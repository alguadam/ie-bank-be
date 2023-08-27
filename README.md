# IE Bank backend

Backend for IE Bank web app

## Configure your local environment

### Configure environment

https://code.visualstudio.com/docs/python/tutorial-flask

1. **Create the virtual environment**. In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select `venv` and then the Python environment you want to use to create it.

### Run and debug

1. **Debug the app locally**. In VS Code, switch to the `Run and Debug` view (using the left-side activity bar or `Ctrl` + `Shift` + `D`). You may see the message "To customize Run and Debug create a launch.json file". S Code can create that for you if you click on the create a launch.json file link:

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
                "FLASK_APP": "run.py",
                "FLASK_DEBUG": "1",
                "ENV": "local",
                "DBUSER":"devuser",
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