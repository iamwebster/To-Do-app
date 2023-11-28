from django.urls import path 
from . import views


urlpatterns = [
    path('', views.notes_view, name='notes'),
    path('add/', views.add_task_view, name='add'),
]