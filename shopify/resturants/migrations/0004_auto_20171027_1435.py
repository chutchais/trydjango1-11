# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0003_auto_20171027_1432'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='RestaurantLocation',
        ),
    ]