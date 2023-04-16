from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("teacher_login", auth_views.LoginView.as_view(template_name='teachers/teacher_login.html'), name='teacher_login'),
    path("teacher_logout", auth_views.LogoutView.as_view(template_name='teachers/teacher_logout.html'), name='teacher_logout'),
    path("teacher_register", views.teacher_register, name='teacher_register'),
    path("teacher_dashboard", views.teacher_dashboard, name='teacher_dashboard'),
    path("teacher_profile/<str:u>/", views.teacher_profile, name='teacher_profile'),
    path("teacher_settings/", views.teacher_settings, name='teacher_settings'),
    path("teacher_requests", views.teacher_requests, name='teacher_requests'),
    

]