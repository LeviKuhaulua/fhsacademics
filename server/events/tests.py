from django.test import TestCase
from .models import Event
import django.utils.timezone as timezone

class EventTestCase(TestCase):
    
    def setUp(self):
        # For reference: meeting_link and resource are optional fields
        Event.objects.create(
            name='All Information', 
            location='McDonalds',
            meeting_link='https://meeting-link.com',
            description='lorem ipsum',
            date=timezone.now(), 
            start='09:00:00', 
            end='10:00:00', 
            resource='https://resource.com'
        )
        Event.objects.create(
            name='Optional Information Excluded',
            location='McDonalds',
            description='lorem ipsum',
            date=timezone.now(),
            start='09:00:00', 
            end='10:00:00',
        )

    def test_slug(self):
        """Verifies that slug is populated when Event object is created"""
        event = Event.objects.get(name='All Information')
        # Grabbing year since Events have the date attribute of the current date
        curr_year = timezone.now().year
        event_name = event.name.replace(' ', '-').lower()
        self.assertEqual(event.slug, f'{event_name}-{curr_year}')

    def test_optional_fields(self):
        """Verifies that there is no error when optional fields are left as blank"""
        event = Event.objects.get(name='Optional Information Excluded')
        self.assertIsInstance(event, Event)
