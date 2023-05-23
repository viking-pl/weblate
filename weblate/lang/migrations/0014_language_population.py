# Generated by Django 4.1a1 on 2022-05-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lang", "0013_alter_plural_formula"),
    ]

    operations = [
        migrations.AddField(
            model_name="language",
            name="population",
            field=models.BigIntegerField(
                default=0,
                help_text="Number of people speaking this language.",
                verbose_name="Number of speakers",
            ),
        ),
    ]
