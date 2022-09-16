# Generated by Django 3.2.15 on 2022-09-16 00:43
import hashid_field.field
from django.db import migrations
from django.db import models

import web.models.sponsor


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0003_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sponsor",
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
                ("link", models.URLField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "logo",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=web.models.sponsor.get_file_path,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]