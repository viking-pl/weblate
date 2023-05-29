# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.2 on 2021-05-07 10:33

import os

from django.conf import settings
from django.db import migrations

from weblate.formats.ttkit import TBXFormat
from weblate.vcs.git import LocalRepository


def migrate_glossaries(apps, schema_editor):
    """
    Removes automatically created glossaries for source language.

    These were wrongly created by 0127_fix_source_glossary since
    0d8b564903518a313d4116ffe82d9c7bc31f7908 - it created blank repo.
    """
    Component = apps.get_model("trans", "Component")
    db_alias = schema_editor.connection.alias

    for component in (
        Component.objects.using(db_alias)
        .filter(is_glossary=True, repo="local:")
        .prefetch_related("project", "source_language")
    ):
        repo_path = os.path.join(
            settings.DATA_DIR, "vcs", component.project.slug, component.slug
        )
        changed = False
        for translation in component.translation_set.select_related("language"):
            if translation.language_id == component.source_language_id:
                continue
            filename = os.path.join(repo_path, translation.filename)

            if os.path.exists(filename):
                continue

            print(f"Adding missing {filename}")

            TBXFormat.create_new_file(filename, translation.language.code, "")
            store = TBXFormat(
                filename,
                language_code=translation.language.code,
                source_language=component.source_language.code,
            )
            store.save()
            changed = True
            # Mark all strings a pending to be committed later
            translation.unit_set.update(
                pending=True,
                details={"add_unit": True},
            )

        if changed:
            repo = LocalRepository(repo_path)
            with repo.lock:
                repo.execute(["add", repo_path])
                if repo.needs_commit():
                    repo.commit("Migrate glossary content")


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0132_alter_unit_state"),
    ]

    operations = [
        migrations.RunPython(
            migrate_glossaries, migrations.RunPython.noop, elidable=True
        )
    ]
