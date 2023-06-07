from django.db import models
from villaowner.models import VillaOwner
class Villa(models.Model):
    villa_owner = models.ForeignKey(VillaOwner, on_delete=models.CASCADE, null= False, blank= False, verbose_name="مالک ویلا")

    description = models.TextField(null=False, blank=False, verbose_name="توضیحات")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت به ازای هرشب")

    created_at = models.DateTimeField(auto_now = True, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="زمان آخرین به روزرسانی")
