# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.5 on 2023-09-18 07:58

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import weblate.auth.models
import weblate.trans.fields
import weblate.utils.fields
import weblate.utils.validators


class Migration(migrations.Migration):
    replaces = [
        (
            "weblate_auth",
            "0002_auto_20180507_1540_squashed_0011_auto_20180509_0739_squashed_0007_group_components",
        ),
        ("weblate_auth", "0008_auto_20200611_1232"),
        ("weblate_auth", "0009_migrate_componentlist"),
        ("weblate_auth", "0010_migrate_componentlist"),
        ("weblate_auth", "0011_unique_case_insensitive"),
        ("weblate_auth", "0012_auto_20200729_1200"),
        ("weblate_auth", "0013_rename_sources_group"),
        ("weblate_auth", "0014_auto_20210512_1955"),
        ("weblate_auth", "0015_userblock"),
        ("weblate_auth", "0016_alter_userblock_unique_together"),
        ("weblate_auth", "0017_alter_user_email"),
        ("weblate_auth", "0018_fixup_role"),
        ("weblate_auth", "0019_alter_role_name"),
        ("weblate_auth", "0020_group_defining_project"),
        ("weblate_auth", "0021_migrate_internal_groups"),
        ("weblate_auth", "0022_alter_user_managers"),
        ("weblate_auth", "0023_user_is_bot"),
        ("weblate_auth", "0024_bot_users"),
        ("weblate_auth", "0025_group_admins"),
        ("weblate_auth", "0026_remove_selection_lists"),
        ("weblate_auth", "0027_alter_group_components"),
        ("weblate_auth", "0028_alter_autogroup_match"),
        ("weblate_auth", "0029_invitation"),
        ("weblate_auth", "0030_alter_invitation_group_alter_user_groups"),
        ("weblate_auth", "0031_alter_userblock_user"),
    ]

    dependencies = [
        ("weblate_auth", "0001_initial"),
        ("lang", "0001_squashed_weblate_5"),
        ("authtoken", "0002_auto_20160226_1747"),
        ("trans", "0001_squashed_weblate_5"),
    ]

    operations = [
        migrations.CreateModel(
            name="Permission",
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
                ("codename", models.CharField(max_length=100, unique=True)),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Permission",
                "verbose_name_plural": "Permissions",
            },
        ),
        migrations.CreateModel(
            name="Role",
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
                (
                    "name",
                    models.CharField(max_length=200, unique=True, verbose_name="Name"),
                ),
                (
                    "permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose permissions granted to this role.",
                        to="weblate_auth.permission",
                        verbose_name="Permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Role",
                "verbose_name_plural": "Roles",
            },
        ),
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=150, verbose_name="Name")),
                (
                    "project_selection",
                    models.IntegerField(
                        choices=[
                            (0, "As defined"),
                            (1, "All projects"),
                            (3, "All public projects"),
                            (4, "All protected projects"),
                            (2, "From component list"),
                        ],
                        default=0,
                        verbose_name="Project selection",
                    ),
                ),
                (
                    "language_selection",
                    models.IntegerField(
                        choices=[(0, "As defined"), (1, "All languages")],
                        default=0,
                        verbose_name="Language selection",
                    ),
                ),
                (
                    "internal",
                    models.BooleanField(
                        default=False, verbose_name="Internal Weblate group"
                    ),
                ),
                (
                    "languages",
                    models.ManyToManyField(
                        blank=True, to="lang.language", verbose_name="Languages"
                    ),
                ),
                (
                    "projects",
                    models.ManyToManyField(
                        blank=True, to="trans.project", verbose_name="Projects"
                    ),
                ),
                (
                    "roles",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose roles granted to this group.",
                        to="weblate_auth.role",
                        verbose_name="Roles",
                    ),
                ),
                (
                    "components",
                    models.ManyToManyField(
                        blank=True, to="trans.component", verbose_name="Components"
                    ),
                ),
                (
                    "componentlists",
                    models.ManyToManyField(
                        blank=True,
                        to="trans.componentlist",
                        verbose_name="Component lists",
                    ),
                ),
                (
                    "defining_project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="defined_groups",
                        to="trans.project",
                    ),
                ),
            ],
            options={
                "verbose_name": "Group",
                "verbose_name_plural": "Groups",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=190,
                unique=True,
                validators=[weblate.utils.validators.EmailValidator()],
                verbose_name="E-mail",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=weblate.auth.models.GroupManyToManyField(
                blank=True,
                help_text="The user is granted all permissions included in membership of these groups.",
                to="weblate_auth.group",
                verbose_name="Groups",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=190,
                null=True,
                unique=True,
                validators=[weblate.utils.validators.EmailValidator()],
                verbose_name="E-mail",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=weblate.utils.fields.EmailField(
                max_length=190,
                null=True,
                unique=True,
                validators=[weblate.utils.validators.EmailValidator()],
                verbose_name="E-mail",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=weblate.utils.fields.UsernameField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Username may only contain letters, numbers or the following characters: @ . + - _",
                max_length=150,
                unique=True,
                validators=[weblate.utils.validators.validate_username],
                verbose_name="Username",
            ),
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "User", "verbose_name_plural": "Users"},
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=weblate.utils.fields.EmailField(
                max_length=190, null=True, unique=True, verbose_name="E-mail"
            ),
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.AddField(
            model_name="user",
            name="is_bot",
            field=models.BooleanField(
                db_index=True, default=False, verbose_name="Robot user"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="date_expires",
            field=models.DateTimeField(
                blank=True, default=None, null=True, verbose_name="Expires"
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="admins",
            field=models.ManyToManyField(
                blank=True,
                help_text="The administrator can add or remove users from a team.",
                related_name="administered_group_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Team administrators",
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="components",
            field=models.ManyToManyField(
                blank=True,
                help_text="Empty selection grants access to all components in project scope.",
                to="trans.component",
                verbose_name="Components",
            ),
        ),
        migrations.CreateModel(
            name="AutoGroup",
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
                (
                    "match",
                    weblate.trans.fields.RegexField(
                        default="^$",
                        help_text="Users with e-mail addresses found to match will be added to this group.",
                        max_length=200,
                        verbose_name="Regular expression for e-mail address",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="weblate_auth.group",
                        verbose_name="Group to assign",
                    ),
                ),
            ],
            options={
                "verbose_name": "Automatic group assignment",
                "verbose_name_plural": "Automatic group assignments",
            },
        ),
        migrations.CreateModel(
            name="Invitation",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "email",
                    weblate.utils.fields.EmailField(
                        blank=True, max_length=190, verbose_name="E-mail"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="User has all possible permissions.",
                        verbose_name="Superuser status",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        help_text="The user is granted all permissions included in membership of these teams.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="weblate_auth.group",
                        verbose_name="Team",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="Please type in an existing Weblate account name or e-mail address.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User to add",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_invitation_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="groups",
            field=weblate.auth.models.GroupManyToManyField(
                blank=True,
                help_text="The user is granted all permissions included in membership of these teams.",
                to="weblate_auth.group",
                verbose_name="Teams",
            ),
        ),
        migrations.CreateModel(
            name="UserBlock",
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
                (
                    "expiry",
                    models.DateTimeField(null=True, verbose_name="Block expiry"),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.project",
                        verbose_name="Project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        db_index=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User to block",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blocked user",
                "verbose_name_plural": "Blocked users",
                "unique_together": {("user", "project")},
            },
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Upper("username"),
                name="weblate_auth_user_username_ci",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Upper("email"),
                name="weblate_auth_user_email_ci",
            ),
        ),
    ]