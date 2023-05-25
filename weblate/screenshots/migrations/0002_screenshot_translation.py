# Generated by Django 3.1.1 on 2020-10-02 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0104_update_source_unit_source"),
        ("screenshots", "0001_squashed_0006_remove_screenshot_sources"),
    ]

    operations = [
        migrations.AddField(
            model_name="screenshot",
            name="translation",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trans.translation",
            ),
        ),
    ]
