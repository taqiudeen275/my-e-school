from django.urls import path
from .views import *

app_name = 'parentUser'
urlpatterns = [
    path('', parentHome, name='index'),
    path('register', parentRegister, name='register'),
    path('user-confirm', verifyStudent, name='verify'),
    path('verified/<int:student>/account', verified, name='complete'),
   
  
]

