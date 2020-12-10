# Generated by Django 3.1.2 on 2020-12-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=150)),
                ('image', models.FileField(upload_to='banner/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
