# Generated by Django 4.0.1 on 2022-03-16 12:09

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserTag",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.CharField(max_length=512, null=True)),
                ("color", models.CharField(max_length=7)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "opencve_users_tags",
            },
        ),
        migrations.CreateModel(
            name="CveTag",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                ("tags", models.JSONField()),
                (
                    "cve",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cve_tags",
                        to="core.cve",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cve_tags",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "opencve_cves_tags",
            },
        ),
        migrations.AddConstraint(
            model_name="usertag",
            constraint=models.UniqueConstraint(
                fields=("name", "user_id"), name="ix_unique_name_userid"
            ),
        ),
        migrations.AddIndex(
            model_name="cvetag",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["tags"], name="ix_cves_tags"
            ),
        ),
    ]
