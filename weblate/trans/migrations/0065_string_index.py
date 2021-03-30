# Generated by Django 3.0.4 on 2020-03-16 05:35

from django.db import migrations


def create_index(apps, schema_editor):
    vendor = schema_editor.connection.vendor
    if vendor == "mysql":
        schema_editor.execute(
            "CREATE INDEX unit_source_index ON trans_unit(source(255))"
        )
        schema_editor.execute(
            "CREATE INDEX unit_context_index ON trans_unit(context(255))"
        )
    elif vendor != "postgresql":
        raise Exception("Unsupported database: {}".format(vendor))


def drop_index(apps, schema_editor):
    vendor = schema_editor.connection.vendor
    if vendor == "mysql":
        schema_editor.execute("ALTER TABLE trans_unit DROP INDEX unit_source_index")
        schema_editor.execute("ALTER TABLE trans_unit DROP INDEX unit_context_index")
    elif vendor != "postgresql":
        raise Exception("Unsupported database: {}".format(vendor))


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0064_fulltext_index"),
    ]

    # This can't be atomic on MySQL
    operations = [
        migrations.RunPython(create_index, drop_index, elidable=False, atomic=False)
    ]
