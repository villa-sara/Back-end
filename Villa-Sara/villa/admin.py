from django.contrib import admin
from .models import Villa, VillaMedia, RentalPeriod


class VillaAdmin(admin.ModelAdmin):
    list_display = ['name', 'villa_owner', 'state', 'city', 'region', 'price_per_night', 'start_date', 'end_date']


class VillaMediaAdmin(admin.ModelAdmin):
    list_display = ['villa', 'created_at']


class RentalPeriodAdmin(admin.ModelAdmin):
    list_display = ['villa', 'start_date', 'end_date']


admin.site.register(Villa, VillaAdmin)
admin.site.register(VillaMedia, VillaMediaAdmin)
admin.site.register(RentalPeriod, RentalPeriodAdmin)
