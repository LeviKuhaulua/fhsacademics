from django.forms import ModelForm, TimeField
from django.forms.widgets import SelectDateWidget, TimeInput
from core.settings import TIME_INPUT_FORMATS

class EventForm(ModelForm):
    
    # Overriding fields in Event Form
    time = TimeField(help_text='Estimated start time. Format: HH:MM AM/PM', input_formats=TIME_INPUT_FORMATS, widget=TimeInput(format='%I:%M %p'))
    end = TimeField(help_text='Estimated end time. Format: HH:MM AM/PM', input_formats=TIME_INPUT_FORMATS, widget=TimeInput(format='%I:%M %p'))

    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.form
        # No need add the model attribute in Meta class as admin will provide both model and fields
        fields = '__all__'
        widgets = {'date': SelectDateWidget}