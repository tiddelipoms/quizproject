# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.TextField(default='/static/madonna.png'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_image',
            field=models.TextField(default='/static/italy.png'),
            preserve_default=False,
        ),
    ]
