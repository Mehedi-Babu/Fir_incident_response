# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir_alerting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytemplate',
            name='body',
            field=models.TextField(help_text=b'This is a Markdown field. You can use django templating language.'),
        ),
    ]
