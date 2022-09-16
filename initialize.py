import os

import django
from django.db import connection
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fc.settings")

django.setup()

from django.contrib.auth import get_user_model  # noqa

INITIALIZE = os.environ.get("INIT_PASS", False)

users = get_user_model().objects.all()

if INITIALIZE:
    print("Initializing")

    try:
        admin_user = get_user_model().objects.create_superuser(
            "rzwink@gmail.com", "rzwink@gmail.com", os.environ.get("INIT_PASS")
        )
        admin_user.save()

    except django.db.utils.IntegrityError:
        pass
