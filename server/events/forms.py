from django.forms import ModelForm, TimeField
from django.forms.widgets import SelectDateWidget, TimeInput
from django.forms import ValidationError
from django.utils.translation import gettext as _
from core.settings import TIME_INPUT_FORMATS

class EventForm(ModelForm):
    
    # Overriding fields in Event Form
    start = TimeField(help_text='Estimated start time. Format: HH:MM AM/PM', input_formats=TIME_INPUT_FORMATS, widget=TimeInput(format='%I:%M %p'))
    end = TimeField(help_text='Estimated end time. Format: HH:MM AM/PM', input_formats=TIME_INPUT_FORMATS, widget=TimeInput(format='%I:%M %p'))

    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.form
        # No need add the model attribute in Meta class as admin will provide both model and fields
        fields = '__all__'
        widgets = {'date': SelectDateWidget}

    def clean(self):
        """
        Does an additional check between the start and end time to ensure 
        that the end time is not the same time as the start time or an earlier time 
        than the start time
        """
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start')
        end_time = cleaned_data.get('end')
        fields_are_empty = start_time is None or end_time is None
        
        # This comparison ensures that the form prevents comparing two NoneType instances
        # In form, this means that your start_time would be 12pm for example, and your end_time would be 11am
        if not fields_are_empty and end_time < start_time:
            raise ValidationError(
                _('End time is before your start time! Value: %(value)s'),
                code='invalid', 
                params={'value': end_time.__format__('%I:%M %p')}, 
            )
        
        # In form, this means that both start_time and end_time are the same time such as 12pm
        if not fields_are_empty and end_time == start_time:
            raise ValidationError(
                _('End time is the same as your start time! Value: %(value)s'),
                code='invalid',
                params={'value': end_time.__format__('%I:%M %p')},
            )
        
        
        
        