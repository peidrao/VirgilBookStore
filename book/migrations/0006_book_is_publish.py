# Generated by Django 4.0.2 on 2022-12-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_remove_book_publication_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_publish",
            field=models.BooleanField(default=False),
        ),
    ]
