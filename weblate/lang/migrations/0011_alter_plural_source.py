# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.2.4 on 2021-08-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lang", "0010_auto_20200627_0508"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plural",
            name="source",
            field=models.SmallIntegerField(
                choices=[
                    (0, "Default plural"),
                    (1, "gettext plural formula"),
                    (3, "stringsdict plural"),
                    (2, "Manually entered formula"),
                ],
                default=0,
                verbose_name="Plural definition source",
            ),
        ),
    ]
