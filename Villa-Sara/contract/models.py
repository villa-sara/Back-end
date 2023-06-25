from django.db import models
from villa.models import Villa, RentalPeriod
from tenant.models import Tenant
from core.models import User


class Contract(models.Model):
    villa = models.OneToOneField(Villa, on_delete=models.CASCADE, primary_key=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host_%(class)s_related',
                             null=False, blank=False, verbose_name="صاحب ملک")
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest_%(class)s_related',
                              null=False, blank=False, verbose_name="میهمان")

    # rental_period = models.ForeignKey(RentalPeriod, on_delete=models.CASCADE,
    #                                   null=False, blank=False, verbose_name="بازه زمانی")
    total_price = models.DecimalField(max_digits=16, decimal_places=4, verbose_name="قیمت کل")
    landowner_phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True,
                                              verbose_name="تلفن همراه مالک")
    people_count = models.PositiveIntegerField(verbose_name="تعداد ساکنین")
    # is_confirmed_by_landowner = models.BooleanField(default=False)
    # is_confirmed_by_tenant = models.BooleanField(default=False)

    start_date = models.DateField(null=False, blank=False, verbose_name="تاریخ شروع اجاره")
    end_date = models.DateField(null=False, blank=False, verbose_name="تاریخ پایان اجاره")

    created_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="زمان آخرین به روزرسانی")

    class Meta:
        verbose_name_plural = "قرارداد"
        verbose_name = "قراردادها"
