from django.contrib import admin
from .models import Event
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['name', 'date', 'duration', 'location', 'meeting_link', 'resource', 'description']
    list_display = ['__str__', 'location', 'date']
    ordering = ['date']