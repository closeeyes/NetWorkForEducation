# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20160530_0911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='readcount',
            new_name='count',
        ),
    ]