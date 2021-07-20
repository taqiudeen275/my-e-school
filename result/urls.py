from django.urls import path
from .views import  *

app_name = 'results'

urlpatterns = [
  path('', results_index, name='home'),
  path('create-report-cards/<int:result_for>/', releaseReportCards, name='create_report'),
  path('create/', create_aboutStudent, name='createAbouts'),
  path('edit-results/<int:result_for>/', fill_abouts, name='fill_abouts'),
  path('edit-results-save', saveAbout, name='save_about'),
  path('all-extra-about-student', all_studentabout_view, name='all_about'),
  path('remarks-delete/<int:id>/',delete_student_remarks, name='da'),
  path('submit-remarks/<int:result_for>/', add_remarks, name='submit_remarks'),
  path('delete-reports/', delete_report_card, name='delete_report_cards'),
  path('delete-report-card-save', delete_reports, name='delete_reports'),


]
