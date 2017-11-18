# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-17 19:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0001_initial'),
        ('assesments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assesment',
            name='subscriber_users',
            field=models.ManyToManyField(to='students.Student'),
        ),
        migrations.AddField(
            model_name='assesment',
            name='updated_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assesments_assesment_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]