# Generated by Django 4.1.5 on 2023-03-09 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekozumi_app', '0003_alter_pet_lastfed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monster',
            old_name='mosterID',
            new_name='monsterID',
        ),
        migrations.AlterField(
            model_name='location',
            name='maxLatitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='maxLongitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='minLatitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='minLongitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='lastFed',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 17, 26, 24, 755511, tzinfo=datetime.timezone.utc)),
        ),
    ]
