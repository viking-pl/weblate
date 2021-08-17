# Generated by Django 3.2.4 on 2021-07-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addons", "0002_cleanup_addon_events"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event",
            field=models.IntegerField(
                choices=[
                    (10, "repository pre-push"),
                    (1, "repository post-push"),
                    (9, "repository pre-update"),
                    (2, "repository post-update"),
                    (3, "repository pre-commit"),
                    (4, "repository post-commit"),
                    (5, "repository post-add"),
                    (6, "unit post-create"),
                    (8, "unit post-save"),
                    (7, "store post-load"),
                    (11, "daily"),
                    (12, "component update"),
                ]
            ),
        ),
    ]
