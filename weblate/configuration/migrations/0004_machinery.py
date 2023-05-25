# Generated by Django 4.1a1 on 2022-05-19 11:26

from django.db import migrations

from weblate.machinery import MACHINE_TRANSLATION_SERVICES

CATEGORY_MT = 2


def migrate_machinery(apps, schema_editor):
    Setting = apps.get_model("configuration", "Setting")

    # TODO: Hardcode defaults in Weblate 5.1
    for name, machinery in MACHINE_TRANSLATION_SERVICES.items():
        Setting.objects.create(
            category=CATEGORY_MT, name=name, value=machinery.migrate_settings()
        )


class Migration(migrations.Migration):

    dependencies = [
        ("configuration", "0003_alter_setting_category"),
        ("trans", "0151_project_machinery_settings"),
    ]

    operations = [migrations.RunPython(migrate_machinery, migrations.RunPython.noop)]
