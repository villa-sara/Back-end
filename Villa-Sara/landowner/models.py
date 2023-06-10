from django.db import models
from django.contrib.auth.models import AbstractUser


class LandOwner(AbstractUser):
    first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name="نام")
    last_name = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام خانوادگی")

    username = models.CharField(max_length=32, null=False, blank=False, unique=True, verbose_name="نام کاربری")
    password = models.CharField(max_length=32, null=False, blank=False, verbose_name="رمز ورود")

    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True, verbose_name="تلفن همراه")
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='ایمیل')

    created_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="زمان آخرین به روزرسانی")

    class Meta:
        verbose_name_plural = "مالکان ویلاها"
        verbose_name = "مالک ویلا"

    def __str__(self):
        return self.username
