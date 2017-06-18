# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloub', '0002_collectpoint_type_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='webacess_tag',
            name='tag_from_type',
            field=models.ForeignKey(to='cloub.Collectpoint_type', null=True, verbose_name='所属采集点'),
        ),
    ]
