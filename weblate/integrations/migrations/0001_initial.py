# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.5 on 2023-09-12 14:28

from django.db import migrations, models
import django.db.models.deletion
import weblate.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trans', '0189_alter_change_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='Integration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('configuration', weblate.utils.fields.JSONField(default={})),
                ('state', weblate.utils.fields.JSONField(default={})),
                ('component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.component')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.project')),
            ],
            options={
                'verbose_name': 'integration',
                'verbose_name_plural': 'integrations',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.IntegerField(choices=[(10, 'repository pre-push'), (1, 'repository post-push'), (9, 'repository pre-update'), (2, 'repository post-update'), (3, 'repository pre-commit'), (4, 'repository post-commit'), (5, 'repository post-add'), (6, 'unit post-create'), (8, 'unit post-save'), (7, 'storage post-load'), (11, 'daily'), (12, 'component update')])),
                ('integration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrations.integration')),
            ],
            options={
                'verbose_name': 'integration event',
                'verbose_name_plural': 'integration events',
                'unique_together': {('integration', 'event')},
            },
        ),
    ]
