# Generated by Django 5.1.3 on 2024-11-15 04:19

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'BookCategory',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('authors', models.ManyToManyField(to='book.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookcategory')),
            ],
            options={
                'db_table': 'Book',
            },
        ),
    ]
