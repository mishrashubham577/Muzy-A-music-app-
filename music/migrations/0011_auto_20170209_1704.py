# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_auto_20170209_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(default=None, null=True, upload_to=b'uploads/'),
        ),
    ]
