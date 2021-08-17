# Generated by Django 3.2.4 on 2021-06-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_auto_20210512_1955"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auditlog",
            name="activity",
            field=models.CharField(
                choices=[
                    ("auth-connect", "auth-connect"),
                    ("auth-disconnect", "auth-disconnect"),
                    ("autocreated", "autocreated"),
                    ("blocked", "blocked"),
                    ("connect", "connect"),
                    ("email", "email"),
                    ("failed-auth", "failed-auth"),
                    ("full_name", "full_name"),
                    ("invited", "invited"),
                    ("locked", "locked"),
                    ("login", "login"),
                    ("login-new", "login-new"),
                    ("password", "password"),
                    ("register", "register"),
                    ("removed", "removed"),
                    ("reset", "reset"),
                    ("reset-request", "reset-request"),
                    ("sent-email", "sent-email"),
                    ("tos", "tos"),
                    ("trial", "trial"),
                    ("username", "username"),
                ],
                db_index=True,
                max_length=20,
            ),
        ),
    ]
