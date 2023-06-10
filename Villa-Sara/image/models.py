from django.db import models
from landowner.models import VillaOwner
from villa.models import Villa


class Image(models.Model):
    image = models.TextField(blank=True, verbose_name="تصویر")
    villa_owner = models.ForeignKey(VillaOwner, on_delete=models.CASCADE, related_name='identity_certification_image',
                                    verbose_name="تصویر کارت ملی یا شناسنامه")
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='villa_images', verbose_name='ویلا')
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name_plural = "تصاویر"
        verbose_name = "تصویر"
