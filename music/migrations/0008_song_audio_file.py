# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audiofield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20170208_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=audiofield.fields.AudioField(help_text=b'Allowed type - .mp3, .wav, .ogg', upload_to=b'your/upload/dir', blank=True),
        ),
    ]
