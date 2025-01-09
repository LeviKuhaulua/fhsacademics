from rest_framework.test import APIClient
from django.test import TestCase
from django.utils import timezone
from events.models import Event
from classes.models import ApClass, GradeLevel, Subject
from datetime import date

class ApiTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        Event.objects.create(
            name='Sample Event', 
            location='Mcdonalds',
            description='Lorem ipsum',
            date=date.today(),
            start=timezone.now(),
            end=timezone.now(), 
        )
        
        # Creating models associated with ApClass
        GradeLevel.objects.create(grade='9')
        Subject.objects.create(subject='Math')

        ApClass.objects.create(
            name='Calculus AB',
            is_offered=True,
            description='Lorem Ipsum',
        )
    
    def test_class_list(self):
        """Verifies that the /classes/ endpoint works"""
        response = self.client.get('/api/classes/')
        self.assertEqual(response.status_code, 200)

    def test_event_list(self):
        """Verifies that the /events endpoint works"""
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, 200)

    def test_class_detail(self):
        """Verifies that the /classes/<slug:slug> endpoint works where slug equals slugified version of class name"""
        
        # Testing endpoint that does not exist
        response = self.client.get('/api/classes/does-not-exist')
        self.assertEqual(response.status_code, 404)
        
        # Adding initial data for mock classes
        ap = ApClass.objects.get(name='Calculus AB')
        ap.grade_level.add(GradeLevel.objects.get(grade='9'))
        ap.subject = Subject.objects.get(subject='Math')
        
        # Testing class that should exist
        response = self.client.get('/api/classes/calculus-ab')
        self.assertEqual(response.status_code, 200)
        

    def test_event_detail(self):
        """Verifies that the /events/<slug:slug> endpoint works where slug equals slugified version of event name and year"""
        
        # Testing endpoint that does not exist
        response = self.client.get('/api/events/does-not-exist')
        self.assertEqual(response.status_code, 404)
        
        # Testing legitimate event
        response = self.client.get('/api/events/sample-event-2025')
        self.assertEqual(response.status_code, 200)