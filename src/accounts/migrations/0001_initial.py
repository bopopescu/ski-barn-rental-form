# Generated by Django 2.2.6 on 2019-10-06 12:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('last_login', models.DateField(default=datetime.datetime(2019, 10, 6, 12, 11, 26, 141511))),
                ('join_date', models.DateField(default=datetime.datetime(2019, 10, 6, 12, 11, 26, 141511))),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[['al', 'Alabama'], ['ak', 'Alaska'], ['az', 'Arizona'], ['ar', 'Arkansas'], ['ca', 'California'], ['co', 'Colorado'], ['ct', 'Connecticut'], ['de', 'Delaware'], ['fl', 'Florida'], ['ga', 'Georgia'], ['hi', 'Hawaii'], ['id', 'Idaho'], ['il', 'Illinois'], ['in', 'Indiana'], ['ia', 'Iowa'], ['ks', 'Kansas'], ['ky', 'Kentucky'], ['la', 'Louisiana'], ['me', 'Maine'], ['md', 'Maryland'], ['ma', 'Massachusetts'], ['mi', 'Michigan'], ['mn', 'Minnesota'], ['ms', 'Mississippi'], ['mo', 'Missouri'], ['mt', 'Montana'], ['ne', 'Nebraska'], ['nv', 'Nevada'], ['nh', 'New Hampshire'], ['nj', 'New Jersey'], ['nm', 'New Mexico'], ['ny', 'New York'], ['nc', 'North Carolina'], ['nd', 'North Dakota'], ['oh', 'Ohio'], ['ok', 'Oklahoma'], ['or', 'Oregon'], ['pa', 'Pennsylvania'], ['ri', 'Rhode Island'], ['sc', 'South Carolina'], ['sd', 'South Dakota'], ['tn', 'Tennessee'], ['tx', 'Texas'], ['ut', 'Utah'], ['vt', 'Vermont'], ['va', 'Virginia'], ['wa', 'Washington'], ['wv', 'West Virginia'], ['wi', 'Wisconsin'], ['wy', 'Wyoming']], default='nj', max_length=200)),
                ('zipCode', models.CharField(max_length=12)),
                ('location', models.IntegerField(choices=[[1, 'Paramus'], [2, 'Wayne'], [3, 'Shrewsbury'], [4, 'Lawrenceville']], default=1)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
