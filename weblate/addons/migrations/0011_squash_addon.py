# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-31 12:45
from __future__ import unicode_literals

from django.db import migrations

from weblate.addons.events import EVENT_POST_COMMIT, EVENT_PRE_PUSH


def update_squash_addon(apps, schema_editor):
    """Update events setup for weblate.git.squash addon."""
    Addon = apps.get_model('addons', 'Addon')
    Event = apps.get_model('addons', 'Event')
    for addon in Addon.objects.filter(name='weblate.git.squash'):
        Event.objects.get_or_create(addon=addon, event=EVENT_POST_COMMIT)
        addon.event_set.filter(event=EVENT_PRE_PUSH).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0010_auto_20181214_1232'),
    ]

    operations = [
        migrations.RunPython(update_squash_addon),
    ]
