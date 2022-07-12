# Generated by Django 3.2.13 on 2022-07-12 20:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('agid', models.AutoField(primary_key=True, serialize=False)),
                ('agentno', models.CharField(max_length=6)),
                ('sido', models.CharField(max_length=2)),
                ('gugun', models.CharField(max_length=4)),
                ('ro', models.CharField(max_length=10)),
                ('agentname', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'agent',
            },
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('appid', models.AutoField(primary_key=True, serialize=False)),
                ('appno', models.CharField(max_length=11)),
                ('pdate', models.DateField(default=datetime.datetime.now)),
                ('fdate', models.DateField()),
                ('edate', models.DateField(default=datetime.datetime.now)),
                ('ptime', models.TimeField()),
                ('insptype', models.CharField(default='', max_length=4)),
                ('msg', models.TextField(null=True)),
                ('fnames', models.CharField(max_length=255, null=True)),
                ('agid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='check.agent')),
            ],
            options={
                'db_table': 'apply',
                'ordering': ['-appno'],
            },
        ),
        migrations.CreateModel(
            name='CenterInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('addr', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('x', models.FloatField(default=0.0)),
                ('y', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'centerinfo',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='InspFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insptype', models.CharField(max_length=4)),
                ('carsize', models.CharField(max_length=2)),
                ('carname', models.CharField(max_length=10)),
                ('fee', models.CharField(max_length=6, null=True)),
            ],
            options={
                'db_table': 'inspfee',
            },
        ),
        migrations.CreateModel(
            name='ApplyUser',
            fields=[
                ('ausrid', models.AutoField(primary_key=True, serialize=False)),
                ('carno', models.CharField(max_length=9)),
                ('appname', models.CharField(max_length=10)),
                ('carname', models.CharField(max_length=10)),
                ('apptel', models.CharField(max_length=10)),
                ('alttel', models.CharField(max_length=10)),
                ('birth', models.CharField(max_length=10)),
                ('addr1', models.CharField(max_length=30)),
                ('addr2', models.CharField(max_length=30)),
                ('appid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='check.apply')),
            ],
            options={
                'db_table': 'applyuser',
            },
        ),
    ]
