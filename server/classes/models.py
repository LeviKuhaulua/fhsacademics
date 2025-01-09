from django.db import models
from django.template.defaultfilters import slugify

class ApClass(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Do not need to put \'AP\' before the class name')
    is_offered = models.BooleanField(default=True, help_text='Check this box if class will be offered for the upcoming school year')
    description = models.TextField(default='', help_text='Description of class')
    grade_level = models.ManyToManyField('GradeLevel')
    prerequisite = models.ManyToManyField('Prerequisite', blank=True)
    benefits = models.TextField(blank=True, help_text='Enter new benefits on a new line')
    student_resource = models.URLField(
        default='', 
        blank=True, 
        help_text='Link for students to access helpful resources of this class if there are any'
    )
    subject = models.ForeignKey(
        'Subject', 
        default='1', 
        on_delete=models.RESTRICT, 
        help_text='Choose the subject that best relates to this class', 
        related_name='+'
    )
    slug = models.SlugField(
        blank=True, 
        unique=True, 
        help_text='''Unique link generated based on class name. 
        Example: classes/calculus instead of classes/9'''
    )
 
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

class Prerequisite(models.Model):
    prerequisite = models.CharField(
        max_length=50, 
        unique=True, 
        null=True, 
        help_text="""Classes needed before a student can apply to the course. 
        Please enter full name of course"""
    )

    def __str__(self):
        return self.prerequisite
    


class Subject(models.Model):   
    subject = models.CharField(max_length=50)


    def __str__(self):
        return self.subject


class GradeLevel(models.Model):
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.grade