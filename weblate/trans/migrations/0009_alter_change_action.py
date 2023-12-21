# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.4 on 2023-12-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0008_workflowsetting"),
    ]

    operations = [
        migrations.AlterField(
            model_name="change",
            name="action",
            field=models.IntegerField(
                choices=[
                    (0, "Resource updated"),
                    (1, "Translation completed"),
                    (2, "Translation changed"),
                    (5, "Translation added"),
                    (3, "Comment added"),
                    (4, "Suggestion added"),
                    (6, "Automatically translated"),
                    (7, "Suggestion accepted"),
                    (8, "Translation reverted"),
                    (9, "Translation uploaded"),
                    (13, "Source string added"),
                    (14, "Component locked"),
                    (15, "Component unlocked"),
                    (17, "Changes committed"),
                    (18, "Changes pushed"),
                    (19, "Repository reset"),
                    (20, "Repository merged"),
                    (21, "Repository rebased"),
                    (22, "Repository merge failed"),
                    (23, "Repository rebase failed"),
                    (28, "Repository push failed"),
                    (24, "Parsing failed"),
                    (25, "Translation removed"),
                    (26, "Suggestion removed"),
                    (27, "Translation replaced"),
                    (29, "Suggestion removed during cleanup"),
                    (30, "Source string changed"),
                    (31, "String added"),
                    (32, "Bulk status changed"),
                    (33, "Visibility changed"),
                    (34, "User added"),
                    (35, "User removed"),
                    (36, "Translation approved"),
                    (37, "Marked for edit"),
                    (38, "Component removed"),
                    (39, "Project removed"),
                    (41, "Project renamed"),
                    (42, "Component renamed"),
                    (43, "Moved component"),
                    (45, "Contributor joined"),
                    (46, "Announcement posted"),
                    (47, "Alert triggered"),
                    (48, "Language added"),
                    (49, "Language requested"),
                    (50, "Project created"),
                    (51, "Component created"),
                    (52, "User invited"),
                    (53, "Repository notification received"),
                    (54, "Translation replaced file by upload"),
                    (55, "License changed"),
                    (56, "Contributor agreement changed"),
                    (57, "Screenshot added"),
                    (58, "Screenshot uploaded"),
                    (59, "String updated in the repository"),
                    (60, "Add-on installed"),
                    (61, "Add-on configuration changed"),
                    (62, "Add-on uninstalled"),
                    (63, "String removed"),
                    (64, "Comment removed"),
                    (65, "Comment resolved"),
                    (66, "Explanation updated"),
                    (67, "Category removed"),
                    (68, "Category renamed"),
                    (69, "Category moved"),
                    (70, "Saving string failed"),
                    (71, "String added in the repository"),
                ],
                default=2,
            ),
        ),
    ]
