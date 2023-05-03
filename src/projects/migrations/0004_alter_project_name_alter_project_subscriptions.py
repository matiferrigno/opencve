# Generated by Django 4.1 on 2023-05-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_project_ix_unique_projects"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="project",
            name="subscriptions",
            field=models.JSONField(default={"products": [], "vendors": []}),
        ),
    ]
