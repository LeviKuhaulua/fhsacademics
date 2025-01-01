from django.contrib import admin
from .models import Event
from datetime import datetime, time
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['name', 'date', 'time', 'end','location', 'meeting_link', 'resource', 'description']
    list_display = ['__str__', 'location', 'get_event_times']
    ordering = ['date']

    @admin.display(description='Event Times')
    def get_event_times(self, obj):
        formatted_date = datetime.strftime(obj.date, '%b %d, %Y')
        formatted_start = time.strftime(obj.time, '%I:%M%p')
        formatted_end = time.strftime(obj.end, '%I:%M%p')
        return f'{formatted_date} from {formatted_start}-{formatted_end}'
    