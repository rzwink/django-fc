# Generated by Django 4.0.2 on 2022-02-07 15:29
import hashid_field.field
from django.db import migrations
from django.db import models

import web.models.product


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=7,
                        prefix="",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("category", models.CharField(blank=True, max_length=20, null=True)),
                ("price", models.CharField(blank=True, max_length=20, null=True)),
                ("brand", models.CharField(blank=True, max_length=20, null=True)),
                ("model", models.CharField(blank=True, max_length=20, null=True)),
                ("condition", models.CharField(blank=True, max_length=20, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=web.models.product.get_file_path,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
