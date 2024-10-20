# Generated by Django 5.1.2 on 2024-10-18 10:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=100, verbose_name='')),
                ('last_name', models.CharField(db_index=True, max_length=100, verbose_name='')),
            ],
            options={
                'verbose_name': 'کارمند',
                'verbose_name_plural': 'کارمندان',
            },
        ),
        migrations.CreateModel(
            name='EntryAndExit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.date.today, verbose_name='تاریخ')),
                ('entry', models.TimeField(blank=True, null=True, verbose_name='ساعت ورود')),
                ('exit', models.TimeField(blank=True, null=True, verbose_name='ساعت خروج')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='home.staff', verbose_name='کارمند')),
            ],
            options={
                'verbose_name': 'ثبت ورود و خروج کارمند',
                'verbose_name_plural': 'ثبت ورود و خروج کارمندان',
                'unique_together': {('staff', 'day')},
            },
        ),
    ]
