from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from . import models
from . import forms


admin.register(models.CustomUser)


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserChangeForm
    form = forms.CustomUserCreationForm
    ordering = ['email']
    fieldsets = (
            (None, {
                'fields':('email', 'password'
                ),
            }),
            ('Details', {
                'fields':('first_name', 'last_name', 'slug'),
            }),
            ('Permissions',{
                'fields':('is_staff','is_active'),
            }),
    )
    