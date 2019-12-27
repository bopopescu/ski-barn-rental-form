# Generated by Django 2.2.6 on 2019-12-04 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='serviceTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_date', models.DateTimeField(auto_now_add=True)),
                ('req_date', models.DateTimeField()),
                ('pickup_date', models.DateTimeField(blank=True)),
                ('ski_model', models.CharField(blank=True, max_length=45)),
                ('ski_make', models.CharField(blank=True, max_length=75)),
                ('binding_model', models.CharField(blank=True, max_length=45)),
                ('binding_make', models.CharField(blank=True, max_length=75)),
                ('boot_model', models.CharField(blank=True, max_length=45)),
                ('boot_make', models.CharField(blank=True, max_length=75)),
                ('service', models.CharField(choices=[['css', 'Complete Shop Service'], ['sws', 'Sharpen Wax Service'], ['other', 'Other']], max_length=20)),
                ('comments', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mountTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_date', models.DateTimeField(auto_now_add=True)),
                ('req_date', models.DateTimeField()),
                ('pickup_date', models.DateTimeField(blank=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('height_inches', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('skiier_type', models.IntegerField(blank=True, choices=[[1, 'Type 1'], [2, 'Type 2'], [3, 'Type 3']])),
                ('stance', models.BooleanField(blank=True, choices=[[True, 'Regular'], [False, 'Goofy']])),
                ('ski_model', models.CharField(max_length=45)),
                ('ski_make', models.CharField(max_length=75)),
                ('binding_model', models.CharField(max_length=45)),
                ('binding_make', models.CharField(max_length=75)),
                ('boot_model', models.CharField(max_length=45)),
                ('boot_make', models.CharField(max_length=75)),
                ('service', models.CharField(blank=True, choices=[['css', 'Complete Shop Service'], ['sws', 'Sharpen Wax Service'], ['other', 'Other']], max_length=20)),
                ('comments', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
