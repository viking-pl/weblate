# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 5.0.3 on 2024-03-27 12:56

from django.db import migrations, models

import weblate.utils.validators


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_alter_auditlog_activity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="codesite",
            field=models.URLField(
                blank=True,
                help_text="Link to your code profile for services like Codeberg or GitLab.",
                validators=[weblate.utils.validators.WeblateURLValidator()],
                verbose_name="Code site URL",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="fediverse",
            field=models.URLField(
                blank=True,
                help_text="Link to your Fediverse profile for federated services like Mastodon or diaspora*.",
                validators=[weblate.utils.validators.WeblateURLValidator()],
                verbose_name="Fediverse URL",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="website",
            field=models.URLField(
                blank=True,
                validators=[weblate.utils.validators.WeblateURLValidator()],
                verbose_name="Website URL",
            ),
        ),
    ]
