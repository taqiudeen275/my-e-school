from django import forms
from .models import StudentUser
from student.models import Student


class SearchByCode(forms.Form):
    code = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'class':'input-material ','placeholder':'Enter Student ID'}
    ))

