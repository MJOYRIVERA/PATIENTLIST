from django import forms
from .models import Patients

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'