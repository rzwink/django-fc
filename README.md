# Django FC
![Django FC - Grandview FC Logo](web/static/web/images/grandview_fc_crest.png "Grandview FC")

Django project supporting Grandview FC. Use app for Django programmers who want to run a basic website for their local soccer/football club. Pulls data dynamically from Teamsnap.

https://www.grandviewfc.org

The application primarily consists of:
* Django
* Bootstrap
* Python



## Installation
1. This is a python + django application.  To get started running locally, you'll need Python3 + Pip (package manager)
   1. Install Python: https://www.python.org/downloads/
   2. Install Pip:
    ```commandline
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    ```
   3. Install Pipenv (this is the newer package manager used by this project)
   ```commandline
    pip install pipenv
   ```
   4. Install Virtualenv (this is so you can install packages in a virtualenv rather than have them running globally)
   ```commandline
    pip install virtualenv
   ```
   5. Go to your favorite projects directory and clone this repo
   6. Create a virtualenv and activate it
   ```commandline
    python -m venv ./venv/
    . ./venv/bin/activate
   ```
   7. This application has a handfull of applications that must be available in your PATH.  While not required,
may cause errors during the next step if not installed.  You can try to skip this step and return to it if the following command fails.
      1. tesseract - see .platform/hooks/postdeploy/install_tesseract.sh or google how best to install tesseract on your platform
      2. developer packages - see .ebextenstions/002_packages.config for packages installed in production by default
   8. Install project dependencies
   ```commandline
    pipenv install
   ```
   9. This project uses pre-commit Black to ensure code formatting standards are adhered.  Do not skip this step:
    ```commandline
    pre-commit install
    ```

2. setup .env by renaming .env.example and adding relevant keys, or receive .env file by
contacting rob@raziexchange.com.  The following commands will not work without a valid .env

3. Initialize a sqlite database
```commandline
python manage.py migrate
```
6. Initialize your database by editing initialize.py to match local credentials you'd like to use
```commandline
python initialize.py
```

8. Start the server
```commandline
python manage.py runserver
```
9. login by accessing https://localhost:8000/    Click Login, enter credentials specified in initialize.py


## Developers
Robert Zwink
