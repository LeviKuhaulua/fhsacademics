from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class ApClass(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=False, unique=True, help_text='Do not need to put \'AP\' before the class name')
    slug = models.SlugField(default='', blank=True, unique=True, help_text='''Unique link generated based on class name. 
                                                                              Example: classes/calculus instead of classes/9''')
    is_active = models.BooleanField(default=True, null=False, help_text='Check if class is offered for the current school year')
    

    def __str__(self):
        '''Returns class name prefixed with 'AP'.'''
        return f'AP {self.name}'
    
    
    def save(self, *args, **kwargs):
        '''Slugifies the class name before saving the object.'''
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    # Meta attributes
    class Meta:
        verbose_name_plural = 'Classes'