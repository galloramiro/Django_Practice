# Generated by Django 2.1.5 on 2019-03-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190327_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen'),
        ),
    ]
