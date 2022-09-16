# Generated by Django 3.2.15 on 2022-09-16 03:26
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0005_news"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="contact",
        ),
        migrations.AddField(
            model_name="news",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
    ]