# Generated by Django 4.1 on 2023-03-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("changes", "0003_alter_change_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="change",
            name="commit",
            field=models.CharField(max_length=40),
        ),
    ]
