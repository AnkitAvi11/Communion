# Generated by Django 3.0.8 on 2020-08-02 23:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20200803_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 23, 26, 8, 274150, tzinfo=utc)),
        ),
    ]