# -*- coding: utf-8 -*-
# Generated by Django 2.0.5 on 2018-06-05 19:25
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("lists", "0002_item_text")]

    operations = [
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        )
    ]
