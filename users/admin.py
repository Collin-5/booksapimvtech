from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomAdmin(admin.ModelAdmin):
    # model = CustomUser
    list_display = ['username', 'email', 'subscribed', 'is_staff', 'is_active']
    # readonly_fields = ['subscribed']
    editable = True
# Register your models here.

admin.site.register(CustomUser, CustomAdmin)
