from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True, verbose_name='نام کاربری')
    is_staff = models.BooleanField(default=False, verbose_name='کارمند')
    is_superuser = models.BooleanField(default=False, verbose_name='مدیر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username} '

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        db_table = 'user'
        ordering = ['created_at']

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True
