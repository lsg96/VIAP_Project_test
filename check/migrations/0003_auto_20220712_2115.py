# Generated by Django 3.2.13 on 2022-07-12 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_alter_apply_ptime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='edate',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='apply',
            name='fdate',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='apply',
            name='pdate',
            field=models.CharField(max_length=10),
        ),
    ]