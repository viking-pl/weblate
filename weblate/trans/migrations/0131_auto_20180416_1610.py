# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 14:10
"""
This contains an ugly hack to workaround Django not handling renaming of
ComponentList.components relation after SubProject -> Component rename.

- temporarily stores component ids in a text field
- removes the relation
- renames the model
- creates relation with new model
- restores id from a text field and drops it
"""

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0011_auto_20180215_1158'),
        ('trans', '0130_auto_20180416_1503'),
        ('addons', '0005_unwrapped_po'),
        ('permissions', '0001_initial'),
        ('screenshots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentlist',
            name='components',
        ),
        migrations.RenameModel(
            old_name='SubProject',
            new_name='Component',
        ),
        migrations.AddField(
            model_name='componentlist',
            name='components',
            field=models.ManyToManyField(blank=True, to='trans.Component'),
        ),
        migrations.AlterModelOptions(
            name='component',
            options={'ordering': ['priority', 'project__name', 'name'], 'permissions': (('lock_component', 'Can lock translation for translating'), ('change_subproject', 'Can change component'), ('can_see_git_repository', 'Can see VCS repository URL'), ('access_vcs', 'Can access VCS repository'), ('view_reports', 'Can display reports')), 'verbose_name': 'Component', 'verbose_name_plural': 'Components'},
        ),
        migrations.RenameField(
            model_name='change',
            old_name='subproject',
            new_name='component',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='subproject',
            new_name='component',
        ),
        migrations.RenameField(
            model_name='translation',
            old_name='subproject',
            new_name='component',
        ),
        migrations.RenameField(
            model_name='whiteboardmessage',
            old_name='subproject',
            new_name='component',
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together=set([('id_hash', 'component')]),
        ),
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together=set([('component', 'language')]),
        ),
    ]
