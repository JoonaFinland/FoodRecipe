# Generated by Django 3.2.4 on 2021-11-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_auto_20211015_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='language',
            field=models.CharField(blank=True, default='en-US', max_length=30),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='credit_month',
            field=models.PositiveIntegerField(default=11),
        ),
    ]