from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    name = forms.CharField(label=False,widget=forms.TextInput(attrs={
      'class':'form-control',
      'placeholder':'Enter your name',
      
      }))
    email = forms.CharField(required=True,label=False,widget=forms.EmailInput(attrs={
         'class':'form-control',
         'placeholder':'Enter your email address',

         
         }))
    message = forms.CharField(label=False,widget=forms.Textarea(
        attrs={

            'class': "form-control ",
            'id': "message",
            'placeholder': 'Enter message'
        }
    ))
    class Meta:
        model = Contact
        fields = '__all__'

 