from django.db import models
from landowner.models import LandOwner
from utilities.constants import STATE_CHOICES
from dynamic_filenames import FilePattern
from core.models import User

image_upload_pattern = FilePattern(filename_pattern='images/{model_name:.30}/{uuid:base32}{ext}')
video_upload_pattern = FilePattern(filename_pattern='videos/{model_name:.30}/{uuid:base32}{ext}')


class Villa(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='نام ملک')
    villa_owner = models.ForeignKey(User, on_delete=models.CASCADE,
                                    null=False, blank=False, verbose_name="صاحب ملک")
    villa_images = []
    state = models.PositiveIntegerField(choices=STATE_CHOICES, verbose_name="استان")
    city = models.CharField(max_length=32, null=False, blank=False, verbose_name="شهر")
    region = models.CharField(max_length=32, null=False, blank=False, verbose_name="منطقه")
    address = models.CharField(max_length=255, null=False, blank=False, verbose_name="آدرس")
    description = models.TextField(max_length=1024, null=False, blank=False, verbose_name="توضیحات")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت به ازای هرشب")
    start_date = models.DateField(null=False, blank=False, verbose_name="تاریخ شروع بازه اجاره")
    end_date = models.DateField(null=False, blank=False, verbose_name="تاریخ پایان بازه اجاره")
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="زمان آخرین به روزرسانی")

    class Meta:
        verbose_name = 'ملک'
        verbose_name_plural = 'املاک'

    def __str__(self):
        return self.name


class VillaMedia(models.Model):
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, null=False, blank=False, verbose_name='ملک')
    villa_image = models.ImageField(upload_to=image_upload_pattern, blank=True, verbose_name='تصویر ملک')
    villa_video = models.FileField(upload_to=video_upload_pattern, blank=True, verbose_name='فیلم ملک')
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name = 'رسانه'
        verbose_name_plural = 'رسانه‌ها'

    def __str__(self):
        return self.villa.name


class RentalPeriod(models.Model):
    start_date = models.DateField(null=False, blank=False, verbose_name="تاریخ شروع اجاره")
    end_date = models.DateField(null=False, blank=False, verbose_name="تاریخ پایان اجاره")
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, null=False, blank=False, verbose_name="ملک")

    class Meta:
        verbose_name = 'بازه زمانی اجاره'
        verbose_name_plural = 'بازه های زمانی اجاره'

    def __str__(self):
        return self.villa.name
