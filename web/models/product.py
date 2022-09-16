import logging
import uuid

from django.db import models
from hashid_field import HashidAutoField

logger = logging.getLogger(__name__)


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return filename


class Product(models.Model):
    id = HashidAutoField(primary_key=True)

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    price = models.CharField(max_length=20, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    file = models.FileField(blank=True, null=True, upload_to=get_file_path)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
