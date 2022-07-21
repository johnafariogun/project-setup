from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from . import models
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    ordering = ['email']
    list_display = ['email','is_active','is_staff','is_superuser']
    search_fields = ['email']
    fieldsets = (
            (None, {'fields':('email', 'password')}),
            ('Details', {'fields':('first_name', 'last_name', 'slug')}),
            ('Permissions',{'fields':('is_staff','is_active')}),
    )


admin.site.register(models.CustomUser) 