# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20170208_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(default=None, null=True, upload_to=b''),
        ),
    ]
