# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='src',
            field=models.ImageField(help_text='Tamano recomendado: 640x640', upload_to='uploads/publi'),
        ),
    ]