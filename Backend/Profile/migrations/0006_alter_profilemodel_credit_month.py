# Generated by Django 3.2.4 on 2021-12-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_auto_20211110_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='credit_month',
            field=models.PositiveIntegerField(default=12),
        ),
    ]
