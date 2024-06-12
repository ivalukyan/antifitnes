from django.contrib import admin
from . import models


# Register your models here.

class SportBotAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'username', 'gender', 'phone_number', 'current_standard']
    list_editable = ['first_name', 'username', 'gender', 'phone_number', 'current_standard']


admin.site.register(models.User, SportBotAdmin)
