# Generated by Django 1.11.16 on 2018-11-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("billing", "0009_auto_20181101_0900")]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="amount",
            field=models.FloatField(default=0),
            preserve_default=False,
        )
    ]
