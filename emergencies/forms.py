from django import forms
from .models import EmergencyIncident, EmergencyResponse

class EmergencyReportForm(forms.ModelForm):
    class Meta:
        model = EmergencyIncident
        fields = ['emergency_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class EmergencyResponseForm(forms.ModelForm):
    class Meta:
        model = EmergencyResponse
        fields = ['response_details']
        widgets = {
            'response_details': forms.Textarea(attrs={'rows': 4}),
        }