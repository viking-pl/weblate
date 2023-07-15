# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-07-29 11:30

from django.db import migrations

CREATE = "CREATE UNIQUE INDEX weblate_auth_user_{0}_ci ON weblate_auth_user(UPPER({0}))"
DROP = "DROP INDEX weblate_auth_user_{0}_ci"


def create_index(apps, schema_editor):
    if schema_editor.connection.vendor == "postgresql":
        schema_editor.execute(CREATE.format("username"))
        schema_editor.execute(CREATE.format("email"))


def drop_index(apps, schema_editor):
    if schema_editor.connection.vendor == "postgresql":
        schema_editor.execute(DROP.format("username"))
        schema_editor.execute(DROP.format("email"))


class Migration(migrations.Migration):
    dependencies = [
        ("weblate_auth", "0010_migrate_componentlist"),
    ]

    operations = [
        migrations.RunPython(create_index, drop_index, elidable=False, atomic=False)
    ]
