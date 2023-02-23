# Generated by Django 4.1.5 on 2023-02-22 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekozumi_app', '0004_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='petType',
            field=models.CharField(choices=[('HEDGEHOG', 'HEDGEHOG'), ('BADGER', 'BADGER'), ('FROG', 'FROG'), ('BAT', 'BAT'), ('WEALSEL', 'WEALSEL'), ('RABBIT', 'RABBIT')], default='HEDGEHOG', max_length=9),
        ),
        migrations.AlterField(
            model_name='pet',
            name='lastFed',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 12, 35, 44, 501637)),
        ),
    ]
