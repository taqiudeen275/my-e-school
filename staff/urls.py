from django.urls import path
from .views import *

app_name = 'staff'
urlpatterns = [
    path('', staffs, name='staffs'),
    path('form-master/', formMaster, name='formMaster'),
    path('teaching-staff/<int:id>/', staffView, name='staff'),
    # Update
    # d -- update --
    path('teaching-staff/<int:id>/update', staff_edit, name='us'),
    
    # Delete
    # d -- delete --
    path('delete/<int:id>/df', deleteformMaster, name='df'),
    path('delete/<int:id>/ds', deleteStaff, name='ds'),
  
]

