# Generated by Django 2.2.6 on 2019-10-06 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191006_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 6, 12, 42, 35, 850009)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2019, 10, 6, 12, 42, 35, 850009)),
        ),
    ]
