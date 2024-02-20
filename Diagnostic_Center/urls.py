from django.urls import path
from Diagnostic_Center import views

app_name = 'Diagnostic_Center'


urlpatterns = [
    path('about/', views.About, name='about'),
    path('view_doctor/', views.View_Doctor, name='view_doctor'),
    path('add_doctor/', views.Add_Doctor, name='add_doctor'),
    #path('delete_doctor(?P<int:pid>)', views.Delete_Doctor, name='delete_doctor'),
    path('view_patient/', views.View_Patient, name='view_patient'),
    path('add_patient/', views.Add_Patient, name='add_patient'),
    #path('delete_patient(?P<int:pid>)', views.Delete_Patient, name='delete_patient'),
    path('view_technician/', views.View_Technician, name='view_technician'),
    path('add_technician/', views.Add_Technician, name='add_technician'),
    #path('delete_technician(?P<int:pid>)', views.Delete_Technician, name='delete_technician'),
]