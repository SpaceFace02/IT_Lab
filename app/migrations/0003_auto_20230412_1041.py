# Generated by Django 2.1.3 on 2023-04-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230412_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='english',
            field=models.IntegerField(default=35, verbose_name='English'),
        ),
        migrations.AddField(
            model_name='item',
            name='maths',
            field=models.IntegerField(default=35, verbose_name='Mathematics'),
        ),
        migrations.AddField(
            model_name='item',
            name='science',
            field=models.IntegerField(default=35, verbose_name='Science'),
        ),
        migrations.AddField(
            model_name='item',
            name='sst',
            field=models.IntegerField(default=35, verbose_name='Social Studies'),
        ),
    ]