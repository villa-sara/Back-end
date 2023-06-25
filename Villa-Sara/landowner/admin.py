from django.contrib import admin
from .models import LandOwner


class LandownerAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user', 'created_at']
    # ['username', 'email', 'first_name', 'last_name', 'phone_number', 'created_at']


admin.site.register(LandOwner, LandownerAdmin)
