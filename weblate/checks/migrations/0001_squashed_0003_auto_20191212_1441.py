# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.6 on 2020-05-27 11:24

import django.db.models.deletion
from django.db import migrations, models

from weblate.checks.models import CHECKS


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("lang", "0001_squashed_0008_auto_20200408_0436"),
        ("trans", "0001_squashed_0074_fix_broken_browser_alert"),
    ]

    operations = [
        migrations.CreateModel(
            name="Check",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "check",
                    models.CharField(
                        choices=CHECKS.get_choices(),
                        max_length=50,
                    ),
                ),
                ("ignore", models.BooleanField(db_index=True, default=False)),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trans.Unit"
                    ),
                ),
            ],
            options={"unique_together": {("unit", "check")}},
        ),
    ]
