# Generated by Django 4.2.2 on 2023-10-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_alumni_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='course',
            field=models.CharField(max_length=255),
        ),
    ]
