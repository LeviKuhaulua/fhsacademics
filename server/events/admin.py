from django.contrib import admin
from .models import Event
from datetime import datetime, time
from .forms import EventForm
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    readonly_fields = ['slug']
    fieldsets = [
        (
            # Important (and minimum) information to create or update object
            'Important Information',
            {
                'fields': [('name', 'date'), 'slug', 'start', 'end', 'location', 'description'],
            }, 
        ), 
        (
            # Can be left out in add or change form
            'Optional Information', 
            {
                'fields': ['meeting_link', 'resource'], 
            }
        )
    ]
    list_display = ['name', 'location', 'get_event_times']
    ordering = ['date']
    search_fields = ['name']
    search_help_text = 'Search for events by name'

    @admin.display(description='Event Times')
    def get_event_times(self, obj):
        # The formatted date would look something like this: Monday Dec 13, 2025
        formatted_date = datetime.strftime(obj.date, '%A %b %d, %Y')
        formatted_start = time.strftime(obj.start, '%I:%M%p')
        formatted_end = time.strftime(obj.end, '%I:%M%p')
        return f'{formatted_date} from {formatted_start}-{formatted_end}'
    