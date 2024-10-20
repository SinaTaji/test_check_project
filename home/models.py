from django.db import models
from datetime import date


class Staff(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='نام', db_index=True)
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی', db_index=True)

    class Meta:
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندان'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EntryAndExit(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='کارمند', db_index=True,
                              related_name='staff')
    day = models.DateField(default=date.today, verbose_name='تاریخ')
    entry = models.TimeField(verbose_name='ساعت ورود', null=True, blank=True)
    exit = models.TimeField(verbose_name='ساعت خروج', null=True, blank=True)

    class Meta:
        verbose_name = 'ثبت ورود و خروج کارمند'
        verbose_name_plural = 'ثبت ورود و خروج کارمندان'

    def __str__(self):
        return f'{self.staff.last_name} - {self.day} - {self.entry} - {self.exit}'

    def is_checked_in(self):
        return self.entry is not None

    def is_checked_out(self):
        return self.exit is not None
