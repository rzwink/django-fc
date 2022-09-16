from django.db import models
from hashid_field import HashidAutoField


class Content(models.Model):
    id = HashidAutoField(primary_key=True)
    slug = models.SlugField()
    content = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
