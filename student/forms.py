from django import forms
from .models import Student,House
from academics.models import Class


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user','my_id', 'completed']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'input-material'}),
            'last_name': forms.TextInput(attrs={'class':'input-material'}),
            'middle_name': forms.TextInput(attrs={'class':'input-material'}),
            # 'photo': forms.FileInput(attrs={'class':'input-material'}),
            'date_of_birth': forms.DateInput(attrs={'class':'input-material','type':'date'}),
            'gender': forms.Select(attrs={'class':'input-material'}),
            'phone_number': forms.NumberInput(attrs={'class':'input-material'}),
            'house': forms.Select(attrs={'class':'input-material'}),
            'accomodation': forms.Select(attrs={'class':'input-material'}),
            'class_info': forms.Select(attrs={'class':'input-material'}),
            'batch': forms.Select(attrs={'class':'input-material'}),
        }

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'input-material'}),
        }

class StudentSearchForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'input-material'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'input-material'}))
    class_info = forms.ModelChoiceField(required=False,queryset=Class.objects.all(),widget=forms.Select(attrs={'class': 'input-material'}))


class ClassStudentSearchForm(forms.Form):
    class_info = forms.ModelChoiceField(required=False, queryset=Class.objects.all(),widget=forms.Select(attrs={'class': 'btn  border-bottom'}))
