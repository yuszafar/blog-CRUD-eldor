# Generated by Django 3.1.3 on 2020-11-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_auto_20201119_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Pic',
        ),
    ]
