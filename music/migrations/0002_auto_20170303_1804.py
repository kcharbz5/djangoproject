# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-03 18:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='logo',
            new_name='album_logo',
        ),
    ]