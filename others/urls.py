from django.urls import path
from .views import *

app_name = 'others'
urlpatterns = [
    path('basics', basicsView, name='basics'),
    path('<int:id>/about-staff', aboutStaffView, name='asd'),
    path('about-staff', aboutStaffaView, name='aboutStaff'),
    path('about-school/', aboutSchoolView, name='aboutSchool'),
    path('about-school/<int:id>', aboutSchoolPost, name='aboutSchoolPost'),
    path('notice-board/', noticeBoardaView, name='noticeBoard'),
    path('<int:id>/notice-board-detail', noticeBoardfView, name='nbd'),
    path('<int:id>/school-history-detail', schoolHistoryView, name='shd'),
    path('<int:id>/notice-board-post', noticeBoardPost, name='nbad'),
    
    # Update
    # u -- update --
    path('update/<int:id>/about-staff',uas , name='uas'),
    path('update/<int:id>/notice-board',unb , name='unb'),
    path('update/<int:id>/school-history',ush , name='ush'),

    # Create
    # s -- save --
    path('create/sp', saveSP, name='ssp'),
    path('create/as', saveAS, name='sas'),
    path('create/nb', saveNB, name='snb'),
    path('create/sh', saveSH, name='ssh'),

    # Delete
    # d -- delete --
    path('delete/<int:id>/sp', deleteSP, name='dsp'),
    path('delete/<int:id>/as', deleteAS, name='das'),
    path('delete/<int:id>/nb', deleteNB, name='dnb'),
    path('delete/<int:id>/sh', deleteSH, name='dsh'),
]
