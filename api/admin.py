from django.contrib import admin
from api.models import *

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    fields = ('name', 'key', 'phone')


@admin.register(DailyMenu)
class DailyMenuAdmin(admin.ModelAdmin):
    fields = ('restaurant', 'day', 'meal')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('restaurant', 'type', 'value')