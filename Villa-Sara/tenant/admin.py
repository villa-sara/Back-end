from django.contrib import admin
from .models import Tenant


class TenantAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user', 'created_at']
    # ['username', 'email', 'phone_number', 'first_name', 'last_name', 'created_at']


admin.site.register(Tenant, TenantAdmin)
