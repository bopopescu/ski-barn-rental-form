# Generated by Django 2.2.6 on 2019-10-06 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('accounts', '0005_auto_20191006_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 6, 13, 39, 56, 822768)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2019, 10, 6, 13, 39, 56, 822768)),
        ),
    ]