import logging
import uuid

from django.db import models
from hashid_field import HashidAutoField

logger = logging.getLogger(__name__)


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return filename


class News(models.Model):
    id = HashidAutoField(primary_key=True)

    headline = models.CharField(max_length=100)
    summary = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    image = models.FileField(blank=True, null=True, upload_to=get_file_path)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
