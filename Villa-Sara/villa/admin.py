from django.contrib import admin
from .models import Villa


class VillaAdmin(admin.ModelAdmin):
    list_display = ['name', 'villa_owner', 'state', 'city', 'region', 'price_per_night']


admin.site.register(Villa, VillaAdmin)
