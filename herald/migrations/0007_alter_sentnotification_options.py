# Generated by Django 4.2.5 on 2023-09-13 11:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("herald", "0006_alter_notification_id_alter_sentnotification_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sentnotification",
            options={
                "verbose_name": "sentnotification",
                "verbose_name_plural": "sentnotifications",
            },
        ),
    ]
