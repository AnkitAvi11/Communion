# Generated by Django 3.0.8 on 2020-08-02 23:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0024_auto_20200726_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='relation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 4, 52, 58, 811648)),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('time_created', models.DateTimeField(default=datetime.datetime(2020, 8, 3, 4, 52, 58, 812645))),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]