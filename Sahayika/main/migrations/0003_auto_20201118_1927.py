# Generated by Django 3.1 on 2020-11-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201118_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='emailid',
            field=models.EmailField(default='xyz@xyz.com', max_length=254),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='emailid',
            field=models.EmailField(default='xyz@xyz.com', max_length=254),
        ),
    ]