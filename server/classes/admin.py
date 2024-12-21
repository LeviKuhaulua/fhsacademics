from django.contrib import admin
from .models import ApClass, GradeLevel, Subject
from django.contrib import messages

# Register your models here.
@admin.register(ApClass, )
class ApClassAdmin(admin.ModelAdmin): 
    # Allows slug to be generated when making a new class
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'subject','is_available']
    actions = ['set_notoffered', 'set_offered']
    filter_horizontal = ['available_to']
    
    
    @admin.display(description="Available Upcoming School Year?", boolean=True, ordering="-is_offered")
    def is_available(self, obj):
        return obj.is_offered

    @admin.action(description='Set as not offered for upcoming school year')
    def set_notoffered(self, request, queryset):
        updates = queryset.update(is_offered=False)
        self.message_user(
            request,
            message = "Unable to make changes" if updates == 0 else "Successfully made changes",
            level = messages.ERROR if updates == 0 else messages.SUCCESS,
        )

    @admin.action(description='Set as offered for upcoming school year')
    def set_offered(self, request, queryset):
        updates = queryset.update(is_offered=True)
        self.message_user(
            request,
            message = "Unable to make changes" if updates == 0 else "Successfully made changes",
            level = messages.ERROR if updates == 0 else messages.SUCCESS,
        )

@admin.register(GradeLevel)
class GradeLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "Farrington AP Administration"
admin.site.site_title = "Farrington Academics"
admin.site.index_title = "Dashboard"