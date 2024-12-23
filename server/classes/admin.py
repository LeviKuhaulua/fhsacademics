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
    actions = ['set_notoffered', 
               'set_offered', 
               'set_available_all', 
               'set_available_9', 
               'set_available_10', 
               'set_available_11', 
               'set_available_12']
    fields = [('name', 'subject'), 'slug', ('is_offered', 'grade_level'), ('description', 'student_resource')]
    filter_horizontal = ['grade_level']
    inlines = [ApClassPrereqsInline, ApClassBenefitsInline]
    list_filter = ['is_offered', 'subject']
    
    @admin.display(description='Available Upcoming School Year?', boolean=True, ordering='-is_offered')
    def is_available(self, obj):
        return obj.is_offered

    @admin.action(description='Set as not offered for upcoming school year')
    def set_notoffered(self, request, queryset):
        updates = queryset.update(is_offered=False)
        self.message_user(
            request,
            message = 'Unable to make changes' if updates == 0 else 'Successfully made changes',
            level = messages.ERROR if updates == 0 else messages.SUCCESS,
        )

    @admin.action(description='Set as offered for upcoming school year')
    def set_offered(self, request, queryset):
        updates = queryset.update(is_offered=True)
        self.message_user(
            request,
            message = 'Unable to make changes' if updates == 0 else 'Successfully made changes',
            level = messages.ERROR if updates == 0 else messages.SUCCESS,
        )
    
    @admin.action(description='Mark selected as available to all grade levels')
    def set_available_all(self, request, queryset):
        all_grade_levels = GradeLevel.objects.all()

        for c in queryset:
            c.grade_level.set(all_grade_levels)
    
    @admin.action(description='Mark selected as available to 9th Grade')
    def set_available_9(self, request, queryset):
        fr = GradeLevel.objects.get(grade='9')

        for c in queryset:
            c.grade_level.add(fr)
    
    @admin.action(description='Mark selected as available to 10th Grade')
    def set_available_10(self, request, queryset):
        so = GradeLevel.objects.get(grade='10')

        for c in queryset:
            c.grade_level.add(so) 
    
    @admin.action(description='Mark selected as available to 11th Grade')
    def set_available_11(self, request, queryset):
        ju = GradeLevel.objects.get(grade='11')

        for c in queryset:
            c.grade_level.add(ju)

    @admin.action(description='Mark selected as available to 12th Grade')
    def set_available_12(self, request, queryset):
        sn = GradeLevel.objects.get(grade='12')

        for c in queryset:
            c.grade_level.add(sn)

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

admin.site.site_header = 'Farrington AP Administration'
admin.site.site_title = 'Farrington Academics'
admin.site.index_title = 'Dashboard'