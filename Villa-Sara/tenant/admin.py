from django.contrib import admin
from .models import Tenant


class TenantAdmin(admin.ModelAdmin):
    pass
    # list_display = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'created_at']


admin.site.register(Tenant, TenantAdmin)
