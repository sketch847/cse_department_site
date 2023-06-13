# Generated by Django 3.2.18 on 2023-06-13 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
