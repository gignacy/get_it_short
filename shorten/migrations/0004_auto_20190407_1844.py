# Generated by Django 2.2 on 2019-04-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0003_auto_20190407_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.CharField(max_length=220),
        ),
        migrations.AlterField(
            model_name='links',
            name='shorten',
            field=models.IntegerField(),
        ),
    ]