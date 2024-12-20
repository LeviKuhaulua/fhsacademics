from django.contrib import admin
from .models import ApClass
from django.contrib import messages

# Register your models here.
class ApClassAdmin(admin.ModelAdmin): 
    # Allows slug to be generated when making a new class
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'is_offered']
    actions = ['set_notoffered', 'set_offered']
    
    @admin.display(description="Offered For Current School Year?", boolean=True)
    def is_offered(self, obj):
        return obj.is_active
    
    @admin.action(description='Set as not offered for current school year')
    def set_notoffered(self, request, queryset):
        updates = queryset.update(is_active=False)
        self.message_user(
            request,
            message = "Unable to make changes" if updates == 0 else "Successfully made changes",
            level = messages.ERROR if updates == 0 else messages.SUCCESS,
        )

    @admin.action(description='Set as offered for current school year')
    def set_offered(self, request, queryset):
        updates = queryset.update(is_active=True)
        self.message_user(
            request,
            message = "Unable to make changes" if updates == 0 else "Successfully made changes",
            level = messages.ERROR if updates == 0 else messages.SUCCESS,
        )


admin.site.register(ApClass, ApClassAdmin)
admin.site.site_header = "Farrington AP Administration"
admin.site.site_title = "Farrington Academics"
admin.site.index_title = "Dashboard"