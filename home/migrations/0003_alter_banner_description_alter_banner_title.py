# Generated by Django 4.0.2 on 2022-12-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_banner_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]