# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('0', '\u7537'), ('1', '\u5973')], default='1', max_length=5),
        ),
    ]
