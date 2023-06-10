from django.contrib import admin
from .models import Villa, VillaMedia


class VillaAdmin(admin.ModelAdmin):
    list_display = ['name', 'villa_owner', 'state', 'city', 'region', 'price_per_night']


class VillaMediaAdmin(admin.ModelAdmin):
    list_display = ['villa']


admin.site.register(Villa, VillaAdmin)
admin.site.register(VillaMedia, VillaMediaAdmin)
