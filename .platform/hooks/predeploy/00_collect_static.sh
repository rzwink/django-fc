#!/bin/bash
source /var/app/venv/*/bin/activate
#python manage.py sqlclear helpdesk
python manage.py migrate
#uncomment when there are new static files
python manage.py collectstatic --noinput
