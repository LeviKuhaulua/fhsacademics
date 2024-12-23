from django.core.management.base import BaseCommand
from classes.models import GradeLevel


class Command(BaseCommand):
    help = 'Create grade levels from 9-12'

    def handle(self, *args, **options):
        try: 
            import core.local_settings
        except ImportError:
            self.stdout.write('Script is intended for local development and if you have the local_settings.py file')

        for _ in ['9', '10', '11', '12']:
            GradeLevel.objects.get_or_create(grade=_)
        
        self.stdout.write('Created grades 9-12 in database')