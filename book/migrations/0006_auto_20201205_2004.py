# Generated by Django 3.1.2 on 2020-12-05 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20201205_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(upload_to='capa/'),
        ),
    ]