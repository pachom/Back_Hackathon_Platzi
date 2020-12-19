"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client', 'is_coach')
    list_filter = ('is_client', 'is_staff', 'is_coach', 'created', 'modified')


admin.site.register(User, CustomUserAdmin)
