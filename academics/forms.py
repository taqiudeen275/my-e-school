from django import forms
from .models import *
from staffUser.models import StaffIDCode


class ProgrammeForm(forms.ModelForm):
    name = forms.CharField(label=False,widget=forms.TextInput(attrs={
      'class':'input-material',
      'placeholder':'Programme Name',
      
      }))
    class Meta:
        model = Programme
        fields = '__all__'

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        widgets = {
            'name': forms.Select(attrs={'class': 'input-material'}),
            'section': forms.Select(attrs={'class': 'input-material'}),
            'batch': forms.Select(attrs={'class': 'input-material'}),
            'track': forms.Select(attrs={'class': 'input-material'}),
        }


class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-material', 'placeholder': 'Enter Form or Level'}),
        }

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-material', 'placeholder':'Enter Batch Name'}),
        }

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-material', 'placeholder':'Enter Semester'}),
        }

class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = Academic_year
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-material', 'placeholder':'Enter Academic Year'}),
        }

class FormMasterForm(forms.ModelForm):
    class Meta:
        model = FormMaster
        fields = '__all__'
        widgets = {
            'staff': forms.Select(attrs={'class': 'input-material'}),
            'clas_s': forms.Select(attrs={'class': 'input-material'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-material', 
            'placeholder': 'Enter Form or Level'
            }),
        }

class StaffUserForm(forms.ModelForm):
    staff_id = forms.CharField(required=False, widget =forms.TextInput(attrs={'class': 'input-material', 'placeholder': 'Staff Id'}))
    phone_number = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'class':'input-material', 'placeholder': 'Phone Number'}))
    date_joined = forms.CharField(required=False, widget=forms.DateInput(attrs={'class':'input-material', 'type':'date'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'input-material', 'placeholder': 'Email'}))
    class Meta:
        model = Staff
        exclude = ['user','verified',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'input-material', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'input-material', 'placeholder': 'Last Name'}),
            'staff_id' : forms.TextInput(attrs={'class': 'input-material', 'placeholder': 'Staff Id'}),
            # 'photo': forms.ImageField(attrs={'class':'input-material'}),
            'gender': forms.Select(attrs={'class':'input-material'}),
            'phone_number': forms.NumberInput(attrs={'class':'input-material', 'placeholder': 'Phone Number'}),
            'class_taught': forms.CheckboxSelectMultiple(attrs={'class':'input-material'}),
            'subject_taught': forms.Select(attrs={'class':'input-material','placeholder': 'Subject Handle'}),
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['user',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'input-material'}),
            'last_name': forms.TextInput(attrs={'class':'input-material'}),
            'staff_id' : forms.TextInput(attrs={'class': 'input-material'}),
            # 'photo': forms.ImageField(attrs={'class':'input-material'}),
            'gender': forms.Select(attrs={'class':'input-material'}),
            'phone_number': forms.NumberInput(attrs={'class':'input-material'}),
            'email': forms.EmailInput(attrs={'class':'input-material'}),
            'date_joined': forms.DateInput(attrs={'class':'input-material', 'type':'date'}),
            'class_taught': forms.CheckboxSelectMultiple(attrs={'class':'input-material'}),
            'subject_taught': forms.Select(attrs={'class':'input-material'}),
        }

class StaffVerifyForm(forms.Form):
    staff_id = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'input_material', 'placeholder': 'Staff Code'}))

class StaffIDCodeForm(forms.ModelForm):
    class Meta:
        model = StaffIDCode
        exclude = ['current']
        widgets = {
            'name': forms.TextInput(attrs={'class':'input-material','placeholder':'Staff Id Code'}),
        }
