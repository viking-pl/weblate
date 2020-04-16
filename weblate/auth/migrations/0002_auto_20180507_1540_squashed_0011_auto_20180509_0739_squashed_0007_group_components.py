# Generated by Django 3.0.5 on 2020-04-21 11:53

import django.db.models.deletion
from django.db import migrations, models

import weblate.auth.models
import weblate.trans.fields
import weblate.utils.validators


class Migration(migrations.Migration):

    replaces = [
        ("weblate_auth", "0002_auto_20180507_1540_squashed_0011_auto_20180509_0739"),
        ("weblate_auth", "0003_auto_20180724_1120"),
        ("weblate_auth", "0004_auto_20180827_1406"),
        ("weblate_auth", "0005_auto_20190516_1153"),
        ("weblate_auth", "0006_auto_20190905_1139"),
        ("weblate_auth", "0007_group_components"),
    ]

    dependencies = [
        ("trans", "0073_auto_20200403_1329"),
        ("lang", "0001_squashed_0008_auto_20200408_0436"),
        ("weblate_auth", "0001_initial"),
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
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose permissions granted to this role.",
                        to="weblate_auth.Permission",
                        verbose_name="Permissions",
                    ),
                ),
            ],
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
                (
                    "name",
                    models.CharField(max_length=150, unique=True, verbose_name="Name"),
                ),
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
                        default=False, verbose_name="Weblate internal group"
                    ),
                ),
                (
                    "componentlist",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.ComponentList",
                        verbose_name="Component list",
                    ),
                ),
                (
                    "languages",
                    models.ManyToManyField(
                        blank=True, to="lang.Language", verbose_name="Languages"
                    ),
                ),
                (
                    "projects",
                    models.ManyToManyField(
                        blank=True, to="trans.Project", verbose_name="Projects"
                    ),
                ),
                (
                    "roles",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose roles granted to this group.",
                        to="weblate_auth.Role",
                        verbose_name="Roles",
                    ),
                ),
                (
                    "components",
                    models.ManyToManyField(
                        blank=True, to="trans.Component", verbose_name="Components"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=190,
                unique=True,
                validators=[weblate.utils.validators.validate_email],
                verbose_name="E-mail",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=weblate.auth.models.GroupManyToManyField(
                blank=True,
                help_text="The user is granted all permissions included in membership of these groups.",
                to="weblate_auth.Group",
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
                validators=[weblate.utils.validators.validate_email],
                verbose_name="E-mail",
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
                        default="^.*$",
                        help_text="Regular expression used to match user e-mail.",
                        max_length=200,
                        verbose_name="E-mail regular expression",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="weblate_auth.Group",
                        verbose_name="Group to assign",
                    ),
                ),
            ],
            options={
                "verbose_name": "Automatic group assignment",
                "verbose_name_plural": "Automatic group assignments",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Mark user as inactive instead of removing.",
                verbose_name="Active",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="User has all possible permissions.",
                verbose_name="Superuser status",
            ),
        ),
    ]
