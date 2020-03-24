# Generated by Django 1.11.13 on 2018-06-21 13:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("wladmin", "0001_initial"),
        ("wladmin", "0002_auto_20180118_1020"),
        ("wladmin", "0003_auto_20180215_1127"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ConfigurationError",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("message", models.TextField()),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("ignored", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-timestamp"]},
        ),
        migrations.AlterIndexTogether(
            name="configurationerror", index_together={("ignored", "timestamp")}
        ),
    ]
