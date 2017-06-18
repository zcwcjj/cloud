# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collectpoint_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.IntegerField(choices=[(0, 'int'), (1, 'float')])),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WebAcess_analog_recorde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.IntegerField()),
                ('tag_name', models.CharField(max_length=30)),
                ('value', models.FloatField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WebAcess_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
                ('owner_equipment', models.ForeignKey(to='cloub.Equipment', verbose_name='所属设备')),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_class',
            field=models.ForeignKey(to='cloub.Equipment_class', verbose_name='所属设备种类'),
        ),
        migrations.AddField(
            model_name='collectpoint_type',
            name='owner_equipment_class',
            field=models.ForeignKey(to='cloub.Equipment_class', verbose_name='所属设备种类'),
        ),
    ]
