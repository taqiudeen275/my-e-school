from django import forms
from academics.models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['user','verified']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'input-material'}),
            'last_name': forms.TextInput(attrs={'class':'input-material'}),
            'gender': forms.Select(attrs={'class':'input-material'}),
            'phone_number': forms.NumberInput(attrs={'class':'input-material'}),
            'email': forms.EmailInput(attrs={'class':'input-material'}),
            'date_joined': forms.DateInput(attrs={'class':'input-material','type': 'date'}),
            'class_taught': forms.SelectMultiple(attrs={'class':'input-material'}),
            'subject_taught': forms.Select(attrs={'class':'input-material'}),
        } 