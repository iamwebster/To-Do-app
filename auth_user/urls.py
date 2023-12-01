from django.urls import path 
from . import views


urlpatterns = [
    path('registration/', views.registration_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]