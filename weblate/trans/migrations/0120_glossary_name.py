# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.4 on 2021-02-17 12:01

from django.db import migrations


def glossary_name(apps, schema_editor):
    Project = apps.get_model("trans", "Project")
    db_alias = schema_editor.connection.alias
    for project in Project.objects.using(db_alias).iterator():
        components = set(project.component_set.values_list("name", flat=True))
        for component in project.component_set.filter(is_glossary=True):
            if component.name == component.glossary_name:
                continue
            newname = component.glossary_name
            if newname in components:
                newname = f"{component.glossary_name} Glossary"
            suffix = 1
            while newname in components:
                newname = f"{component.glossary_name} Glossary {suffix}"
                suffix += 1

            component.name = newname
            component.save(update_fields=["name"])
            components.add(newname)


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0119_auto_20210206_1141"),
    ]

    operations = [
        migrations.RunPython(glossary_name, migrations.RunPython.noop, elidable=True)
    ]
