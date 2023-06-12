from django.db import models
from villa.models import Villa
from contract.models import Contract

class RentalPeriod():
    start_date = models.DateField(null=False, blank=False, verbose_name="تاریخ شروع اجاره")
    end_date = models.DateField(null=False, blank=False, verbose_name="تاریخ پایان اجاره")

    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, null=False, blank=False, verbose_name="ملک")

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=False, blank=False, verbose_name="قرارداد")

    class Meta:
        verbose_name = 'قرارداد'
        verbose_name_plural = 'قراردادها'