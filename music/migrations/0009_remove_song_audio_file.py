# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_song_audio_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audio_file',
        ),
    ]
