from django import forms
from .models import *
from froala_editor.widgets import FroalaEditor


class StaffPositionForm(forms.ModelForm):
    class Meta:
        model = StaffPosition
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-material'}),
        }

class AboutStaffForm(forms.ModelForm):
    discription = FroalaEditor()
    class Meta:
        model = AboutStaff
        fields = '__all__'
        widgets = {
            'staff': forms.Select(attrs={'class': 'input-material'}),
            'year_employed': forms.DateInput(attrs={'class': 'input-material','type':'date'}),
            'position': forms.Select(attrs={'class': 'input-material'}),
        }

class NoticeBoardForm(forms.ModelForm):
    body = FroalaEditor()
    class Meta:
        model = NoticeBoard
        fields = '__all__'
        widget = {
            'title': forms.TextInput(attrs={'class':'input-material'})
        }

class SchoolHistoryForm(forms.ModelForm):
    body = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = SchoolHistory
        fields = '__all__'
        widget = {
            'title': forms.TextInput(attrs={'class':'input-material'}),
            
        } 