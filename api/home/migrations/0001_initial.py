# Generated by Django 5.0.1 on 2024-01-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=250)),
                ("image", models.FileField(upload_to="images/banner")),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=30)),
                ("subject", models.CharField(blank=True, max_length=100)),
                ("email", models.CharField(blank=True, max_length=100)),
                ("message", models.TextField(blank=True, max_length=300)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("New", "New"),
                            ("Read", "Read"),
                            ("Closed", "Closed"),
                        ],
                        default="New",
                        max_length=6,
                    ),
                ),
                ("ip", models.CharField(blank=True, max_length=20)),
                ("note", models.CharField(blank=True, max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]