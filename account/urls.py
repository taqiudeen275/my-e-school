from django.urls import path
from .views import *



app_name = 'account'
urlpatterns = [
    path('', loginView, name='login'),
    path('signup/', signupView , name='register'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile-save-staff-info', saveStaff, name='saveStaff'),
    path('profile-save-student-info', saveStudent, name='saveStudent'),
    path('change-user-type/',change_userType , name='changeUT'),
    
]
