from django.contrib import admin

from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display=('name','email','resume')


admin.site.register(UserInfo,UserInfoAdmin)
