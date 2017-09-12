# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 08:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_credituser_is_submitted'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='credituser',
            unique_together=set([('credit_group', 'email', 'is_admin')]),
        ),
    ]
