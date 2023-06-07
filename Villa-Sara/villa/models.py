from django.db import models
from .. villaowner.models import VillaOwner
from .. utilities.constants import STATE_CHOICES


class Villa(models.Model):
    villa_owner = models.ForeignKey(VillaOwner, on_delete=models.CASCADE, null= False, blank= False, verbose_name="مالک ویلا")

    state = models.PositiveIntegerField(choices=STATE_CHOICES, verbose_name="استان")
    city = models.CharField(max_length=32, null=False, blank=False, verbose_name="شهر")
    region = models.CharField(max_length=32, null=False, blank=False, verbose_name="منطقه")
    address = models.CharField(max_length=255, null=False, blank=False, verbose_name="آدرس")
    description = models.TextField(max_length=1024, null=False, blank=False, verbose_name="توضیحات")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت به ازای هرشب")

    created_at = models.DateTimeField(auto_now = True, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="زمان آخرین به روزرسانی")
