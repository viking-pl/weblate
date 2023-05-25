# Generated by Django 3.0.5 on 2020-05-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0076_comment_userdetails"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="announcement",
            name="message_html",
        ),
        migrations.AlterField(
            model_name="announcement",
            name="message",
            field=models.TextField(
                help_text="You can use Markdown and mention users by @username.",
                verbose_name="Message",
            ),
        ),
    ]
