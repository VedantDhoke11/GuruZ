from django import forms
from .models import Pandit

class PanditRegistrationForm(forms.ModelForm):
    class Meta:
        model = Pandit
        fields = ['name', 'experience', 'contact_info', 'location', 'specialization', 'languages', 'availability', 'email',]
