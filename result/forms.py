from django import forms
from django.forms import modelformset_factory
from academics.models import Academic_year,Semester,Subject
from .models import *
from .models import Result as Results

# class CreateResults(forms.ModelForm):
#     class Meta:
#         model = Result
#         fields = '__all__'
#         widget = {
#             'semester': forms.Select(attrs={'class':'form-control'})
#             'academic_year': forms.Select(attrs={'class':'form-control'})
#         }
  
# subjectResult = modelformset_factory(SubjectResult, fields=('test_1_score','test_2_score','Mid_Semester_score', 'exam_score'), extra=0, can_delete=True)


class SubjectForm(forms.ModelForm):
    prefix = 'Subject'
    class Meta:
        model = Subject
        fields = ['name']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'
        widget = {
            'semester': forms.Select(attrs={'class':'form-control'}),
            'academic_year': forms.Select(attrs={'class':'form-control'})
        }

class CreateResults(forms.Form):
  result_for = forms.ModelChoiceField(queryset=Results.objects.all())
  subjects = forms.ModelMultipleChoiceField(
      queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple)

EditSubjectResults = modelformset_factory(SubjectResult, fields=('test_1_score', 'test_2_score', 'mid_semester_score', 'exam_mark', 'absent'), extra=0, can_delete=True)
EditAboutStudent = modelformset_factory(AboutStudent, fields=('conduct', 'attitude', 'interest','remarks'), extra=0, can_delete=True)
DeleteReportCards = modelformset_factory(ReportCard, fields=('student',), extra=0, can_delete=True)

class CreateResultStaffUser(forms.Form):
  result_for = forms.ModelChoiceField(queryset=Results.objects.all())

