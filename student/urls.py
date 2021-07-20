from django.urls import path
from .views import *

app_name = 'student'
urlpatterns = [
    path('', students, name='students'),
    path('<int:id>/student-detail', studentView, name='student'),

    # Update 
    # u -- update --
    path('student/<int:id>/update', student_edit, name='us'),

    # Delete
    # d -- delete --
    path('delete/<int:id>/ds', deleteStudent, name='ds'),
  
]

