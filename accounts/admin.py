from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'is_staff', 'is_active', 'is_superuser')
    list_editable = ('is_staff', 'is_active', 'is_superuser')
    list_display_links = ('username', 'email')


admin.site.register(User, UserAdmin)
