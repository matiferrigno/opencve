# Generated by Django 4.1 on 2023-03-09 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("advisories", "0002_alter_advisory_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advisory",
            name="key",
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
