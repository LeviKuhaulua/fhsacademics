from django.db import models

# Create your models here.
class ApClass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, unique=True, help_text='Do not need to put \'AP\' before the class name.')
    is_active = models.BooleanField(default=True, null=False)
    
    def __str__(self):
        return f'AP {self.name}'
    
    # Meta attributes
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"