# Generated by Django 4.1 on 2023-03-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("changes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="change",
            name="task",
        ),
        migrations.AddField(
            model_name="change",
            name="commit",
            field=models.CharField(default="", max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name="change",
            name="path",
            field=models.TextField(default=None, null=True),
        ),
    ]
