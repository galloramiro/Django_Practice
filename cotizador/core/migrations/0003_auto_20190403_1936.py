# Generated by Django 2.1.5 on 2019-04-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190403_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisors',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='advisors',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Teléfono'),
        ),
    ]
