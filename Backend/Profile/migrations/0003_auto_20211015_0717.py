# Generated by Django 3.2.4 on 2021-10-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20211012_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='calendar',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='recordings',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
