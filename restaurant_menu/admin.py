from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status") #database fields
    list_filter = ("status", )
    search_fields = ("mean", "description")


admin.site.register(Item, MenuItemAdmin)
