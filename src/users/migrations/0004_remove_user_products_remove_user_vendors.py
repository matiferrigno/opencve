# Generated by Django 4.1 on 2023-04-13 21:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_usertag_color_alter_usertag_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="products",
        ),
        migrations.RemoveField(
            model_name="user",
            name="vendors",
        ),
    ]
