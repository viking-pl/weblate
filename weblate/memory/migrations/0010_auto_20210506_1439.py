# Generated by Django 3.2 on 2021-05-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memory", "0009_pg_index"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memory",
            name="from_file",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="memory",
            name="shared",
            field=models.BooleanField(default=False),
        ),
    ]
