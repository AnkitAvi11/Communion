# Generated by Django 3.0.8 on 2020-07-22 18:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20200718_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_date', models.DateTimeField(default=datetime.datetime(2020, 7, 22, 23, 36, 7, 610938))),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_set', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]