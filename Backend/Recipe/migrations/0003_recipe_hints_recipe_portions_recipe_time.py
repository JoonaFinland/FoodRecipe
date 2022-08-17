# Generated by Django 4.0.4 on 2022-06-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0002_alter_ingredient_name_alter_ingredient_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='hints',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='portions',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(default=20),
        ),
    ]
