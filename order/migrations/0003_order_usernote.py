# Generated by Django 3.1.2 on 2020-12-15 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201205_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='usernote',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]