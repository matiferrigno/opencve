# Generated by Django 4.1 on 2023-05-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_integration"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="project",
            constraint=models.UniqueConstraint(
                fields=("name", "user_id"), name="ix_unique_projects"
            ),
        ),
    ]
