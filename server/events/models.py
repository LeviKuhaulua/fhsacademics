from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(verbose_name='Event Name', max_length=150, help_text='Max character limit: 150')
    location = models.CharField(verbose_name='Event Location', max_length=75, help_text='Please put formal name. Max character limit: 75')
    meeting_link = models.URLField(blank=True, default='', help_text='Online meeting link. Can be left empty')
    description = models.TextField()
    date = models.DateTimeField(verbose_name='Event Date and Start Time')
    duration = models.DurationField(help_text='Estimated length of event')
    resource = models.URLField(default='', blank=True, help_text="""Public resource link for students, 
                                                                    parents, and faculty that cannot make 
                                                                    it to event. Can be left empty""")
    

    def __str__(self):
        """Returns event name followed by the year that the event is being held"""
        return f'{self.name} {self.date.year}'