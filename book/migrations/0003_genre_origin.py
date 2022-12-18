# Generated by Django 4.0.2 on 2022-12-16 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre_origin', to='book.genre'),
        ),
    ]
