# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.0.1 on 2022-01-26 08:23

from django.db import migrations


def migrate_internal_groups(apps, schema_editor):
    Group = apps.get_model("weblate_auth", "Group")

    groups = (
        Group.objects.using(schema_editor.connection.alias)
        .filter(internal=True, name__contains="@")
        .prefetch_related("projects")
    )

    for group in groups:
        projects = group.projects.all()
        if len(projects) != 1:
            raise ValueError(
                f"Internal group {group.name} has more than one project assigned!"
            )
        group.defining_project = projects[0]
        group.name = group.name.split("@")[1]
        group.save(update_fields=["defining_project", "name"])


class Migration(migrations.Migration):
    dependencies = [
        ("weblate_auth", "0020_group_defining_project"),
    ]

    operations = [migrations.RunPython(migrate_internal_groups, elidable=True)]
