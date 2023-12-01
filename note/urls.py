from django.urls import path 
from . import views


urlpatterns = [
    path('', views.notes_view, name='notes'),
    path('add/', views.add_task_view, name='add'),
    path('task/<int:pk>/', views.detail_task_view, name='detail'),
    path('task/<int:pk>/delete', views.delete_task_view, name='delete'),
    path('completed/', views.completed_tasks_views, name='completed'),
    path('completed/task/<int:pk>/', views.detail_complete_task, name='detail_complete'),
    path('task/<int:pk>/edit/', views.edit_task_view, name='edit'),
    path('filter/<str:imp>/', views.category, name='importance_choose')
]