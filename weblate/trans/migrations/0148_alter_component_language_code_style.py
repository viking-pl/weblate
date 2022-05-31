# Generated by Django 4.0.2 on 2022-03-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0147_delete_projecttoken"),
    ]

    operations = [
        migrations.AlterField(
            model_name="component",
            name="language_code_style",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Default based on the file format"),
                    ("posix", "POSIX style using underscore as a separator"),
                    ("bcp", "BCP style using hyphen as a separator"),
                    (
                        "posix_long",
                        "POSIX style using underscore as a separator, including country code",
                    ),
                    (
                        "bcp_long",
                        "BCP style using hyphen as a separator, including country code",
                    ),
                    ("android", "Android style"),
                    ("java", "Java style"),
                    ("linux", "Linux style"),
                ],
                default="",
                help_text="Customize language code used to generate the filename for translations created by Weblate.",
                max_length=10,
                verbose_name="Language code style",
            ),
        ),
    ]
