# Generated by Django 3.2.13 on 2022-07-13 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0006_auto_20220713_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='atame',
            new_name='atname',
        ),
    ]
