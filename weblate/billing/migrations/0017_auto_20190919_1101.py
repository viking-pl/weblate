# Generated by Django 2.2.5 on 2019-09-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("billing", "0016_auto_20190911_1316")]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="expiry",
            field=models.DateTimeField(
                blank=True,
                default=None,
                help_text="After expiry removal with 15 days grace period is scheduled.",
                null=True,
                verbose_name="Trial expiry date",
            ),
        ),
        migrations.AlterField(
            model_name="billing",
            name="removal",
            field=models.DateTimeField(
                blank=True,
                default=None,
                help_text="This is automatically set after trial expiry.",
                null=True,
                verbose_name="Scheduled removal",
            ),
        ),
    ]
