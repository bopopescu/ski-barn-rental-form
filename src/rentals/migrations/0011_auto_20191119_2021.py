# Generated by Django 2.2.6 on 2019-11-20 01:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0010_auto_20191119_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='input_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 19, 20, 21, 16, 696900)),
        ),
    ]
