from django.contrib import admin
from .models import SpaceObject

@admin.register(SpaceObject)
class SpaceObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',  'distance', 'size')
    search_fields = ('name', 'category')


