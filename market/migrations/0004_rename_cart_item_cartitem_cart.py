# Generated by Django 4.0.2 on 2022-12-31 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0003_remove_cart_cart_item_cartitem_cart_item"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitem",
            old_name="cart_item",
            new_name="cart",
        ),
    ]