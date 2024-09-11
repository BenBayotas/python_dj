from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('subjects/', views.subjects, name="subjects"),
    path('teachers/', views.teachers, name="teachers"),
    path('rooms/', views.rooms, name="rooms"),
]
