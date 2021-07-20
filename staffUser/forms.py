from django import forms 
from academics.models import Academic_year
from result.models import Result


class SearchByRF(forms.Form):
    academic_year = forms.ModelChoiceField(queryset=Result.objects.all())