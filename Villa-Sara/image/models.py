from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime

from villaowner.models import VillaOwner


class Image(models.Model):
    image = models.TextField(blank=True, verbose_name="تصویر")
    villa_owner = models.ForeignKey(VillaOwner, on_delete=models.CASCADE, related_name='identity_certification_image',
                                    verbose_name="تصویر کارت ملی یا شناسنامه")

    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name_plural = "تصاویر"
        verbose_name = "تصویر"

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.now()
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.title
