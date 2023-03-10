# Generated by Django 4.1.4 on 2022-12-27 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2022, 12, 27, 3, 10, 44, 49536, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='activity',
            name='endTime',
            field=models.TimeField(default=datetime.datetime(2022, 12, 27, 3, 10, 44, 49536, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='activity',
            name='frequency',
            field=models.CharField(default='once', max_length=50),
        ),
        migrations.AddField(
            model_name='activity',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2022, 12, 27, 3, 10, 44, 49536, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='activity',
            name='startTime',
            field=models.TimeField(default=datetime.datetime(2022, 12, 27, 3, 10, 44, 49536, tzinfo=datetime.timezone.utc)),
        ),
    ]
