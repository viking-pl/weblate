# Generated by Django 3.0.7 on 2020-06-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_profile_nearby_strings"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="onetime",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="notification",
            field=models.CharField(
                choices=[
                    ("MergeFailureNotification", "Repository failure"),
                    ("RepositoryNotification", "Repository operation"),
                    ("LockNotification", "Component locking"),
                    ("LicenseNotification", "Changed license"),
                    ("ParseErrorNotification", "Parse error"),
                    ("NewStringNotificaton", "New string"),
                    ("NewContributorNotificaton", "New contributor"),
                    ("NewSuggestionNotificaton", "New suggestion"),
                    ("LastAuthorCommentNotificaton", "Comment on own translation"),
                    ("MentionCommentNotificaton", "Mentioned in comment"),
                    ("NewCommentNotificaton", "New comment"),
                    ("ChangedStringNotificaton", "Changed string"),
                    ("TranslatedStringNotificaton", "Translated string"),
                    ("ApprovedStringNotificaton", "Approved string"),
                    ("NewTranslationNotificaton", "New language"),
                    ("NewComponentNotificaton", "New translation component"),
                    ("NewAnnouncementNotificaton", "New announcement"),
                    ("NewAlertNotificaton", "New alert"),
                    ("PendingSuggestionsNotification", "Pending suggestions"),
                    ("ToDoStringsNotification", "Strings needing action"),
                ],
                max_length=100,
            ),
        ),
    ]
