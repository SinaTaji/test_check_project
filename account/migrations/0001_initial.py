# Generated by Django 5.1.2 on 2024-10-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='نام کاربری')),
                ('is_staff', models.BooleanField(default=False, verbose_name='کارمند')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='مدیر')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
                'db_table': 'user',
                'ordering': ['created_at'],
            },
        ),
    ]
