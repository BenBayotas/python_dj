from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('ga_module/', views.ga_module, name='ga_module'),
    path('ga_module/subject_details/<int:id>', views.subject_details, name='subject_details'),
    path('testing/', views.testing, name='testing'),
    
]