# Generated by Django 3.2.13 on 2022-07-13 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_auto_20220712_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='agid',
            new_name='agid_id',
        ),
    ]
