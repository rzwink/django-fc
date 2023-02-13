from django.db import models
from hashid_field import HashidAutoField


class Contact(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=120)

    email = models.EmailField(max_length=120)
    message = models.TextField()
