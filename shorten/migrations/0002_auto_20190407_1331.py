# Generated by Django 2.2 on 2019-04-07 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='link',
            new_name='post',
        ),
    ]
