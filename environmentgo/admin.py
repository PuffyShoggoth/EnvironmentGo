from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)

    def username(self, obj):
        return obj.user.username
    username.admin_order_field = 'user__username'

admin.site.register(Profile, ProfileAdmin)