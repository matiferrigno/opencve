# Generated by Django 4.1 on 2023-03-09 23:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("advisories", "0003_alter_advisory_key"),
    ]

    operations = [
        migrations.RenameField(
            model_name="advisory",
            old_name="original_url",
            new_name="link",
        ),
    ]
