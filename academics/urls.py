from django.urls import path
from .views import *

app_name = 'academics'
urlpatterns = [
    path('basics', basics, name='basics'),
    # Create
    # s -- save --
    path('basics/create/sa', saveAy, name='sa'),
    path('basics/create/sb', saveBatch, name='sb'),
    path('basics/create/sc', saveClass, name='sc'),
    path('basics/create/ssj', saveSubject, name='ssj'),
    path('basics/create/sl', saveLevel, name='sl'),
    path('basics/create/ss', saveSemester, name='ss'),
    path('basics/create/sp', saveProgram, name='sp'),
    path('basics/create/sr', saveResultFOr, name='sr'),
    path('basics/create/sh', saveHouse, name='sh'),
    path('basics/create/ssid', saveStaffID, name='ssid'),

    # Delete
    # d -- delete --
     path('basics/delete/<int:id>/da', deleteAy, name='da'),
    path('basics/delete/<int:id>/db', deleteBatch, name='db'),
    path('basics/delete/<int:id>/dc', deleteClass, name='dc'),
    path('basics/delete/<int:id>/dsj', deleteSubject, name='dsj'),
    path('basics/delete/<int:id>/dl', deleteLevel, name='dl'),
    path('basics/delete/<int:id>/ds', deleteSemester, name='ds'),
    path('basics/delete/<int:id>/dp', deleteProgram, name='dp'),
    path('basics/delete/<int:id>/dh', deleteHouse, name='dh'),
    path('basics/delete/<int:id>/dr', deleteResult, name='dr'),
    path('basics/delete/<int:id>/dsid', deleteStaffId, name='dsid'),

    path('basics/delete/<int:id>/dsid', deleteStaffId, name='dsid'),
    path('basics/change-class', classChange, name='changeClass'),

]

