# Generated by Django 5.1.2 on 2024-10-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='last_name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='نام خانوادگی'),
        ),
    ]
