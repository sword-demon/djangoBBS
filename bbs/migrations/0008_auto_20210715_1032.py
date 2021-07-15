# Generated by Django 2.2 on 2021-07-15 10:32

import bbs.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0007_auto_20210714_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.FileField(default='/avatars/avatar.jpg', storage=bbs.storage.ImageStorage(), upload_to='avatar/%Y%m'),
        ),
    ]