from django.contrib import admin
from . models import UserModel
# from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(UserModel)
# admin.site.register(UserModel)
# @admin.register(UserModel)
# class AdminUserModel(UserAdmin)
    # list_display = ['password']
    
    # list_display = ['id', "username", 'phone', 'otp_enabled',
    #               'otp_verified', 'otp_base32', 'otp_auth_url']


