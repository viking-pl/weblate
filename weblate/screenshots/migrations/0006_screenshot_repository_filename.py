# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1.7 on 2023-05-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screenshots", "0005_alter_screenshot_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="screenshot",
            name="repository_filename",
            field=models.CharField(
                blank=True,
                help_text="Scan for screenshot file change on repository update.",
                max_length=200,
                verbose_name="Repository path to screenshot",
            ),
        ),
    ]
