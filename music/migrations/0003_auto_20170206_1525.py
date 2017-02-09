# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170206_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_type', models.CharField(max_length=200, null=True, blank=True)),
                ('song_title', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='album',
        ),
        migrations.RemoveField(
            model_name='album',
            name='album_text',
        ),
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='album_title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(to='music.Album'),
        ),
    ]
