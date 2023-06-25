from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    """
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': (
            'username',
        )}),
    )
    """
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {"classes": ("wide",),
                "fields": ("email", "first_name", "last_name"),
                }),
    )


admin.site.register(User, UserAdmin)
