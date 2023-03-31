from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("request/", views.request, name="request"),
    path('view_requests/', views.view_requests, name="view_requests"),
    path('profile/<str:u>/', views.profile, name="profile"),
    path("settings/", views.settings, name="settings"),
    path("delete_course/", views.delete_course, name="delete_course"),
    path("fees/", views.fees, name="fees"),
    path("online_class", views.online_class, name="online_class"),
    path("exam/", views.exam, name='exam'),
    path("voting/", views.voting, name='voting'),
    path("enrollment/", views.enrollment, name="enrollment"),
    path("add_course/", views.add_course, name='add_course'),

]