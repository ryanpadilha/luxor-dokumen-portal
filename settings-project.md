#### Configuring the development environment

For all developer >:D

Pre-requisites
- Any flavor of Linux OS
- Python 3.x
- pip (last version)

We suggest PyCharm IDE for Python development, some settings for coding is needed as follow:

1. Inside the project of any application it's recommend to create a folder
named 'venv-scripts' that's contains the main script to create the
virtual environment (virtualenv) with all dependencies.

The main script invoke 'venv' tool to create the local environment,
isolating the development libraries per project; also invoke 'pip install'
with 'requirements.txt' file to install related dependencies.

2. As soon as possible, execute the script 'venv.sh' on terminal,
that's will create a 'venv-sandbox' folder on the root project structure.
After, on IDE select the menu 'file > settings', on the left side bar,
search for 'Project Interpreter'.

On this item we have the selected project interpreter, then select
the recently created by the step 1, and click on 'apply'
button for confirm the configuration.

To run the application, the best approach is to edit run configuration
and create the runner just for this project.

Select the menu 'run > edit configurations', on the screen showed,
click on the '+' (plus sign), that's will create a proper configuration to
run the application, fill the main fields as required:
- Name: the name of the runner.
- Script: select the 'run.py' file (entry point of application).
- Python Interpreter: the python interpreter configured in settings.
- Working directory: the directory of the project.

Confirm the configuration clicking on 'apply' button.
Finally, for testing the environment, click on the start button (shift + F10),
on the console the result of execution is exhibit.