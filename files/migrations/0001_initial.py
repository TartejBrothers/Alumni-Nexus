# Generated by Django 4.2.2 on 2023-10-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('degree', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
