# Generated by Django 2.1.5 on 2019-04-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190403_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisors',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Mails'),
        ),
    ]
