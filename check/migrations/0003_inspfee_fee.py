# Generated by Django 3.2.13 on 2022-07-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_auto_20220711_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspfee',
            name='fee',
            field=models.CharField(max_length=6, null=True),
        ),
    ]