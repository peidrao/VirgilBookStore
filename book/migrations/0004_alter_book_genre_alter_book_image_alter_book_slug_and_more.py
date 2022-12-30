# Generated by Django 4.0.2 on 2022-12-18 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("book", "0003_genre_origin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="book.genre"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.FileField(null=True, upload_to="images/capa"),
        ),
        migrations.AlterField(
            model_name="book",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="status",
            field=models.IntegerField(choices=[(1, "Yes"), (2, "Not")], default=1),
        ),
        migrations.AlterField(
            model_name="book",
            name="writer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="book.writer",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="book",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="book.book"
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="status",
            field=models.IntegerField(
                choices=[(1, "New"), (2, "Read"), (3, "Trash")], default=1
            ),
        ),
        migrations.AlterField(
            model_name="images",
            name="book",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="book.book"
            ),
        ),
        migrations.AlterField(
            model_name="writer",
            name="image",
            field=models.FileField(null=True, upload_to="images/writer"),
        ),
        migrations.AlterField(
            model_name="writer",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
