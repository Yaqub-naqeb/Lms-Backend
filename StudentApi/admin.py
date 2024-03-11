from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'address']

admin.site.register(Profile, ProfileAdmin)

