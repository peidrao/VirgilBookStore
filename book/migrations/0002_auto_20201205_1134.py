# Generated by Django 3.1.2 on 2020-12-05 14:34

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0004_auto_20201204_2231'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='book.genre'),
        ),
        migrations.AddField(
            model_name='genre',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('keywords', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('image', models.FileField(upload_to='book/')),
                ('price', models.FloatField()),
                ('amount', models.IntegerField()),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('Sim', 'True'), ('Não', 'False')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genre', models.ManyToManyField(to='book.Genre')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer.writer')),
            ],
        ),
    ]