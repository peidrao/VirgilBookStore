# Generated by Django 5.0.1 on 2024-01-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("code", models.CharField(editable=False, max_length=5)),
                ("first_name", models.CharField(max_length=10)),
                ("last_name", models.CharField(max_length=10)),
                ("phone", models.CharField(blank=True, max_length=11)),
                ("address", models.CharField(blank=True, max_length=150)),
                ("city", models.CharField(max_length=100)),
                ("total", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Novo", "Novo"),
                            ("Aceitaram", "Aceitaram"),
                            ("Prepararam", "Prepararam"),
                            ("Enviaram", "Enviaram"),
                            ("Concluído", "Concluído"),
                            ("Cancelaram", "Cancelaram"),
                        ],
                        default="Novo",
                        max_length=10,
                    ),
                ),
                ("ip", models.CharField(blank=True, max_length=20)),
                ("adminnote", models.CharField(blank=True, max_length=100)),
                ("usernote", models.CharField(blank=True, max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrderBook",
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
                ("quantity", models.IntegerField()),
                ("price", models.FloatField()),
                ("amount", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Novo", "Novo"),
                            ("Aceitaram", "Aceitaram"),
                            ("Cancelaram", "Cancelaram"),
                        ],
                        default="Novo",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ShopCart",
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
                ("quantity", models.IntegerField()),
            ],
        ),
    ]
