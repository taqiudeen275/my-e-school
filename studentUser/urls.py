from django.urls import path
from .views import *

app_name = 'studentUser'
urlpatterns = [
    path('', studentHome, name='index'),
    path('register', studentRegister, name='register'),
    path('user-confirm', verifyStudent, name='verify'),
    path('all-student-id', allStudentID, name='allstudentsId'),
    path('verified/<int:student>/account', verified, name='complete'),
   
  
]

