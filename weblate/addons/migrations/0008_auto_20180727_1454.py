# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("addons", "0007_auto_20180629_1736")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event",
            field=models.IntegerField(
                choices=[
                    (1, "post push"),
                    (2, "post update"),
                    (3, "pre commit"),
                    (4, "post commit"),
                    (5, "post add"),
                    (6, "unit post create"),
                    (8, "unit post save"),
                    (7, "store post load"),
                ]
            ),
        )
    ]
