from django.core.management.base import BaseCommand
from classes.models import Subject

class Command(BaseCommand):
    help = 'Creates the initial subjects based on already available classes. INTENDED FOR LOCAL DEVELOPMENT'
    
    def handle(self, *args, **options):

        try:
            import core.local_settings
        except ImportError:
            self.stdout.write('Unable to import local settings')

        for _ in ['Math', 'Science', 'English', 'Arts', 'Social Studies']:
            Subject.objects.get_or_create(subject = _)

        self.stdout.write('Created inital subjects')
