from django.contrib import admin
from .models import ApClass

# Register your models here.
class ApClassAdmin(admin.ModelAdmin): 
    # Allows slug to be generated when making a new class
    prepopulated_fields = {'slug': ['name']}

admin.site.register(ApClass, ApClassAdmin)
admin.site.site_header = "Farrington AP Administration"
admin.site.site_title = "Farrington Academics"
admin.site.index_title = "Dashboard"