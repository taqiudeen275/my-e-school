from django.urls import path
from .views import *

app_name = 'staffUser'
urlpatterns = [
    path('index', staffHome, name='home'),
    path('staff/register', staffRegister, name='register'),
    path('staff/verify', verifyStaff, name='verify'),
    path('create/', create_result, name='createResults'),
    path('edit-results/<int:result_for>/', fill_results, name='fill_scores'),
    path('edit-results-save', saveSubjectResult, name='save_scores'),
    path('view/all', all_results_view, name='allResults'),
    path('submit/<int:result_for>/', assignSubjectPosition, name='completed'),

]
