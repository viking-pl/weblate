# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-09-04 09:21

import json

from django.db import migrations


def fix_enforced_checks(apps, schema_editor):
    Component = apps.get_model("trans", "Component")
    db_alias = schema_editor.connection.alias
    for component in Component.objects.using(db_alias).filter(
        enforced_checks__contains="'"
    ):
        component.enforced_checks = json.loads(
            component.enforced_checks.replace("'", '"')
        )
        component.save(update_fields=["enforced_checks"])


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0095_fix_json_units"),
    ]

    operations = [
        migrations.RunPython(
            fix_enforced_checks, migrations.RunPython.noop, elidable=True
        ),
    ]
