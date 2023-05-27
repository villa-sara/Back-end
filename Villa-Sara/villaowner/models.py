from django.db import models
from django.utils import timezone

from jdatetime import datetime as jdatetime_datetime

class VillaOwner(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name="نام")
    last_name = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام خانوادگی")

    username = models.CharField(max_length=32, null=False, blank=False, unique=True, verbose_name="نام کاربری")
    password = models.CharField(max_length=32, null=False, blank=False, verbose_name="رمز ورود")

    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True, verbose_name="تلفن همراه")

    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name_plural = "مالکان ویلاها"
        verbose_name = "مالک ویلا"

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.phone_number}"

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        super().save(*args, **kwargs)
