# Generated by Django 4.0.1 on 2022-03-14 19:03

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import changes.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Change",
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
                ("json", models.JSONField()),
                (
                    "cve",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="changes",
                        to="core.cve",
                    ),
                ),
            ],
            options={
                "db_table": "opencve_changes",
            },
        ),
        migrations.CreateModel(
            name="Task",
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
                (
                    "nvd_checksum",
                    models.CharField(
                        default=changes.models.get_random_sha256,
                        max_length=64,
                        unique=True,
                    ),
                ),
            ],
            options={
                "db_table": "opencve_tasks",
            },
        ),
        migrations.CreateModel(
            name="Event",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("new_cve", "New CVE"),
                            (
                                "first_time",
                                "Vendors/Products appeared for the first time",
                            ),
                            ("references", "References changed"),
                            ("cpes", "CPEs changed"),
                            ("cvss", "CVSS changed"),
                            ("summary", "Summary changed"),
                            ("cwes", "CWEs changed"),
                        ],
                        default="new_cve",
                        max_length=10,
                    ),
                ),
                ("details", models.JSONField()),
                ("is_reviewed", models.BooleanField(default=False)),
                (
                    "change",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="changes.change",
                    ),
                ),
                (
                    "cve",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="core.cve",
                    ),
                ),
            ],
            options={
                "db_table": "opencve_events",
            },
        ),
        migrations.AddField(
            model_name="change",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="changes",
                to="changes.task",
            ),
        ),
    ]
