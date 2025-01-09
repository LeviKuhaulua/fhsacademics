from django.test import TestCase
from .models import ApClass, Subject, Prerequisite, GradeLevel

class ApClassTestCase(TestCase):
    
    def setUp(self):
        Subject.objects.create(subject='Test')
        GradeLevel.objects.bulk_create(
            [
                GradeLevel(grade='9'),
                GradeLevel(grade='10'),
                GradeLevel(grade='11'),
                GradeLevel(grade='12'), 
            ]
        )
        Prerequisite.objects.bulk_create(
            [
                Prerequisite(prerequisite='Math'),
                Prerequisite(prerequisite='Science'), 
                Prerequisite(prerequisite='English')
            ]
        )
        # As reference, model has the following optional fields
        # prerequisite, benefits, student_resource, slug (but not really)
        ApClass.objects.create(
            name='Class Test',
            is_offered=True,
            description='Lorem ipsum',
            subject=Subject.objects.get(subject='Test'),
        )

    def test_slug_on_save(self):
        """Verifies that slug field gets populated when object is saved"""
        class_test = ApClass.objects.get(name='Class Test')
        class_test.grade_level.set(GradeLevel.objects.all())
        class_test.prerequisite.set(Prerequisite.objects.all())
        self.assertEqual(class_test.slug, 'class-test')   

    def test_str(self):
        """Verifies that __str__ method has AP prefixed to the name"""
        class_test = ApClass.objects.get(name='Class Test')
        self.assertEqual(class_test.__str__(), 'AP Class Test')

