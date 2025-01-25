from django.forms import ModelForm,DateInput, NumberInput, Select,TimeInput,TextInput,IntegerField
from django.core.exceptions import ValidationError
from .models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'  # Include all fields from the Meeting model
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter meeting title'}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time':TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'duration': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in hours'}),
            'room': Select(attrs={'class': 'form-control'}),
        }
