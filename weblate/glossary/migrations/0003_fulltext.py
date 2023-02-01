# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.6 on 2020-06-10 11:50

from django.db import migrations

FIELDS = (
    ("term", "source"),
    ("term", "target"),
)

PG_TRGM = "CREATE INDEX {0}_{1}_fulltext ON glossary_{0} USING GIN ({1} gin_trgm_ops)"
PG_DROP = "DROP INDEX {0}_{1}_fulltext"

MY_FTX = "CREATE FULLTEXT INDEX {0}_{1}_fulltext ON glossary_{0}({1})"
MY_DROP = "ALTER TABLE glossary_{0} DROP INDEX {0}_{1}_fulltext"


def create_index(apps, schema_editor):
    vendor = schema_editor.connection.vendor
    if vendor == "postgresql":
        # Create GIN trigram index on searched fields
        for table, field in FIELDS:
            schema_editor.execute(PG_TRGM.format(table, field))
    elif vendor == "mysql":
        for table, field in FIELDS:
            schema_editor.execute(MY_FTX.format(table, field))
    else:
        raise Exception(f"Unsupported database: {vendor}")


def drop_index(apps, schema_editor):
    vendor = schema_editor.connection.vendor
    if vendor == "postgresql":
        for table, field in FIELDS:
            schema_editor.execute(PG_DROP.format(table, field))
    elif vendor == "mysql":
        for table, field in FIELDS:
            schema_editor.execute(MY_DROP.format(table, field))
    else:
        raise Exception(f"Unsupported database: {vendor}")


class Migration(migrations.Migration):
    dependencies = [
        ("glossary", "0002_migrate_dictionary"),
    ]

    operations = [
        migrations.RunPython(create_index, drop_index, elidable=False, atomic=False)
    ]
