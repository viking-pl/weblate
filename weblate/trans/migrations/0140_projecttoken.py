# Generated by Django 3.2.5 on 2021-07-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0139_alter_component_repoweb"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectToken",
            options={
                "verbose_name": "Project Token", 
                "verbose_name_plural": "Project Tokens",
                "unique_together": {("project", "token")},
            },
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "token",
                    models.CharField(
                        help_text="Token value to use in API",
                        max_length=100,
                        verbose_name="Token value",
                    ),
                ),
                ("expires", models.DateTimeField(verbose_name="Expires")),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=models.deletion.CASCADE, to="trans.project"
                    ),
                ),
            ],
        ),
    ]
