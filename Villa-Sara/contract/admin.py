from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ['villa', 'host', 'guest', 'total_price', 'landowner_phone_number',
                    'people_count', 'start_date', 'end_date']


admin.site.register(Contract, ContractAdmin)
