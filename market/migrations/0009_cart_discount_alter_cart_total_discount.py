# Generated by Django 4.1.4 on 2023-01-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0008_cart_total_discount"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="discount",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="cart",
            name="total_discount",
            field=models.FloatField(default=0),
        ),
    ]
