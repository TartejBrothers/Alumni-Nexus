# Generated by Django 4.2.2 on 2023-10-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='course',
            field=models.CharField(default='CSE', max_length=255),
        ),
    ]
