# Generated by Django 3.2.13 on 2022-07-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_inspfee_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sido', models.CharField(max_length=2)),
                ('gugun', models.CharField(max_length=4)),
                ('ro', models.CharField(max_length=10)),
                ('agentname', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'agent',
            },
        ),
    ]
