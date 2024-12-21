from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class ApClass(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Do not need to put \'AP\' before the class name')
    slug = models.SlugField(blank=True, unique=True, help_text='''Unique link generated based on class name. 
                                                                              Example: classes/calculus instead of classes/9''')
    is_offered = models.BooleanField(default=True, help_text='Check this box if class will be offered for the upcoming school year')
    description = models.TextField(default='', help_text='Description of class')
    subject = models.ForeignKey('Subject', 
                                default='1', 
                                on_delete=models.RESTRICT, 
                                help_text='Choose the subject that best relates to this class', 
                                related_name='+')
    grade_levels = models.ManyToManyField('GradeLevel')
    student_resource = models.URLField(blank=True, help_text='Link for students to access helpful resources of this class if there are any')

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

class ApClassPrereq(models.Model):
    # Model to create the many-to-one relationship
    ap = models.ForeignKey(ApClass, on_delete=models.CASCADE, default='1', null=False, related_name='prereqs')
    prerequisite = models.CharField(max_length=50, blank=True, unique=True, null=True, help_text="""Classes needed before a student can apply to the course. 
                                                                                        Please enter full name of course""")

    def __str__(self):
        return self.prerequisite
    
    class Meta: 
        verbose_name = 'Pre-requisite'


class ApClassBenefit(models.Model):
    # Model to create the many-to-one relationship
    ap = models.ForeignKey(ApClass, on_delete=models.CASCADE, related_name='benefit')
    benefit = models.CharField(max_length=75, blank=True, unique=True, null=True, help_text='character limit: 75')

    def __str__(self):
        return self.benefit

class Subject(models.Model):   
    subject = models.CharField(max_length=50)


    def __str__(self):
        return self.subject


class GradeLevel(models.Model):
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.grade