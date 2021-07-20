from django import forms
from .models import User
from django.contrib.auth import  authenticate,login,logout




class SignupForm(forms.ModelForm):

   first_name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'first_name',
      'placeholder': 'first name'
      
      }))
   last_name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'last_name',
      'placeholder':'last name'
      }))
   email = forms.CharField(required=False,widget=forms.EmailInput(attrs={
         'class':'input-material',
         'id':'email',
         'placeholder': 'email address'

         
         }))      
   username = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'"username',
      'placeholder':'username'
      
      }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
      'class':'input-material',
      'id':'password',
       'name':'password',
       'placeholder': 'password'
         
      }))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={
      'class':'input-material',
      'id':'password2',
       'name':'password2',
      'placeholder': 'confirm password'
      }))
   user_type =forms.ChoiceField(widget=forms.Select(
      attrs={'class':'input-material', 'id':'userType', 'placeholder': 'user type'}
    ), choices=User.userType_select)

   gender =forms.ChoiceField(widget=forms.Select(
      attrs={'class':'input-material', 'id':'userType', 'placeholder': 'user type'}
    ), choices=User.gender_select)
   
   class Meta:
      model = User
      fields=[
         'first_name',
         'last_name',
         'email',
         'username',    
         'password',
         'password2',
         'user_type'
      ]
     

   def clean(self,*args, **kwargs):
         password = self.cleaned_data.get('password')
         password2 = self.cleaned_data.get('password2')
         email = self.cleaned_data.get('email')
         username = self.cleaned_data.get('username')
         if password != password2:
            raise forms.ValidationError('password not matching')
         if email != '':
            emailqs = User.objects.filter(email=email)
            if emailqs.exists():
               raise forms.ValidationError('Email is already being used')
         usernameqs = User.objects.filter(username=username)
         if usernameqs.exists():
            raise forms.ValidationError('This user name is already being user you can put your email ')
         return super(SignupForm,self).clean(*args, **kwargs)
  

class LoginForm(forms.Form):
   username = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'login-username',
      "name":"Username",
      'placeholder': 'Username or Email',
      'data-msg':"Please enter your username"
      }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
      'class':'input-material',
      'id':'login-password',
       'name':'Password',
       'placeholder': 'Password'
         
      }))

   def clean(self,*args, **kwargs):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')

      if username and password:
         user = authenticate(username=username,password=password)
         if not user:
            raise forms.ValidationError('Incorrect Username or Password')
         

      return super(LoginForm,self).clean(*args, **kwargs)


class ProfileForm(forms.ModelForm):

   first_name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'first_name',
      'placeholder': 'first name'
      
      }))
   last_name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'last_name',
      'placeholder':'last name'
      }))
   email = forms.CharField(required=False,widget=forms.EmailInput(attrs={
         'class':'input-material',
         'id':'email',
         'placeholder': 'email address'

         
         }))      
   username = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'"username',
      'placeholder':'username'
      
      }))
   
   user_type =forms.ChoiceField(widget=forms.Select(
      attrs={'class':'input-material', 'id':'userType', 'placeholder': 'user type'}
    ), choices=User.userType_select)

   gender =forms.ChoiceField(widget=forms.Select(
      attrs={'class':'input-material', 'id':'userType', 'placeholder': 'user type'}
    ), choices=User.gender_select)
   
   class Meta:
      model = User
      fields=[
         'first_name',
         'last_name',
         'email',
         'username',   
         'gender', 
         'user_type',
         'photo'
      ]

      def clean(self,*args, **kwargs):
         email = self.cleaned_data.get('email')
         username = self.cleaned_data.get('username')
         if email != '':
            emailqs = User.objects.filter(email=email)
            if emailqs.exists():
               raise forms.ValidationError('Email is already being used')
         usernameqs = User.objects.filter(username=username)
         if usernameqs.exists():
            raise forms.ValidationError('This user name is already being user you can put your email ')
         return super(ProfileForm,self).clean(*args, **kwargs)
  


class ChangeUTForm(forms.ModelForm):
   user_type =forms.ChoiceField(widget=forms.Select(
      attrs={'class':'input-material', 'id':'userType', 'placeholder': 'user type'}
    ), choices=User.userType_select)
   class Meta:
      model = User
      fields=[
         'user_type',
      ]
