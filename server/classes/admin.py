from django.contrib import admin
from .models import ApClass

# Register your models here.
class ApClassAdmin(admin.ModelAdmin):
    pass

admin.site.register(ApClass, ApClassAdmin)