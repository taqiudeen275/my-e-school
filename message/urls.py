from django.urls import path
from .views import *

app_name = 'message'
urlpatterns = [
    path('studeent-report-cards', studentReportCards, name='studentReportCard'),
    path('wards-report-cards', parentReportCards, name='parentReportCard'),
    path('studeent-report-card/<int:id>/view/', reportCard, name='reportCard'),

]

