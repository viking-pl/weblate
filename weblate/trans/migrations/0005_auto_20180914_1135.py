# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-14 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0004_project_use_shared_tm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='branch',
            field=models.CharField(blank=True, default='', help_text='Repository branch to translate', max_length=200, verbose_name='Repository branch'),
        ),
    ]
