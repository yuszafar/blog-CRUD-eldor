# Generated by Django 3.1.3 on 2020-11-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20201119_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='pic',
            name='width',
            field=models.IntegerField(blank=True),
        ),
    ]
