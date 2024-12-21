from django.contrib import admin
from .models import ApClass, ApClassPrereq, ApClassBenefit, GradeLevel, Subject 
from django.contrib import messages

class ApClassPrereqsInline(admin.StackedInline):
    model = ApClassPrereq

class ApClassBenefitsInline(admin.StackedInline):
    model = ApClassBenefit

# Register your models here.
@admin.register(ApClass)
class ApClassAdmin(admin.ModelAdmin): 
    # Allows slug to be generated when making a new class
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'subject','is_available']
    actions = ['set_notoffered', 'set_offered']
    fields = [('name', 'subject'), 'slug', ('is_offered', 'grade_levels'), ('description', 'student_resource')]
    filter_horizontal = ['grade_levels']
    inlines = [ApClassPrereqsInline, ApClassBenefitsInline]
    
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
    actions = None
    
    # Grade Levels are ALWAYS consistent, therefore no need to modify them in any way. 
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    actions = None

admin.site.site_header = "Farrington AP Administration"
admin.site.site_title = "Farrington Academics"
admin.site.index_title = "Dashboard"