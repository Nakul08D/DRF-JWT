from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomBaseUser

class CustomBaseUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('email',)
    search_fields = ('email',)


    # Define the fields to be displayed in the change form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
     # Define the fields to be displayed in the add form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )

admin.site.register(CustomBaseUser, CustomBaseUserAdmin)