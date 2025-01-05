from django.db import models
from datetime import time
from django.template.defaultfilters import slugify

# Create your models here.
class Event(models.Model):
    name = models.CharField(verbose_name='Event Name', max_length=150, help_text='Max character limit: 150')
    slug = models.SlugField(default='', max_length=75, help_text='Unique link generated based on event name and year. Example: events/parent-night-2025 vs events/1')
    location = models.CharField(verbose_name='Event Location', max_length=75, help_text='Please put formal name. Max character limit: 75')
    meeting_link = models.URLField(blank=True, default='', help_text='Online meeting link. Can be left empty')
    description = models.TextField()
    date = models.DateField(help_text='Date Event')

    # Default attribute is set to prevent django from telling us that not having a default value will cause database issues 
    # I should probably make my own custom Model Field to handle this, but that's a problem for another day
    start = models.TimeField(default=time.min, verbose_name='Start Time', help_text='Time that the event starts')
    end = models.TimeField(default=time.min, verbose_name='End Time', help_text='Estimated time event will end')
    
    resource = models.URLField(default='', blank=True, help_text="""Public resource link for students, 
                                                                    parents, and faculty that cannot make 
                                                                    it to event. Can be left empty""")
    

    def __str__(self):
        """Returns event name"""
        return self.name
    
    def save(self, *args, **kwargs):
        """Slugifies the event before saving the object"""
        event_name = f'{self.name} {self.date.year}'
        self.slug = slugify(event_name)
        super().save(*args, **kwargs)
        