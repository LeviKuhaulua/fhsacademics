from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class ApClass(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True, help_text='Do not need to put \'AP\' before the class name')
    slug = models.SlugField(default='', blank=True, unique=True, help_text='''Unique link generated based on class name. 
                                                                              Example: classes/calculus instead of classes/9''')
    is_offered = models.BooleanField(default=True, null=False, help_text='Check this box if class is offered for the current school year')
    description = models.TextField(default='', null=False, help_text='Description of class')
    subject = models.ForeignKey('Subject', 
                                default='1', 
                                null=False, 
                                on_delete=models.PROTECT, 
                                help_text='Choose the subject that best relates to this class', 
                                related_name='+')
    available_to = models.ManyToManyField('GradeLevel')
 

    def __str__(self):
        """Returns class name prefixed with 'AP'."""
        return f'AP {self.name}'
    
    
    def save(self, *args, **kwargs):
        """Slugifies the class name before saving the object."""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    # Meta attributes
    class Meta:
        verbose_name = 'AP'

class Subject(models.Model):   
    subject = models.CharField(max_length=50)


    def __str__(self):
        return self.subject


class GradeLevel(models.Model):
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.grade