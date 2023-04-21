from django.urls import path
from . import views

urlpatterns = [
    path("make_post/", views.make_post, name='make_post'),
    path("users_make_post/", views.make_post, name='make_post'),
    path("post_like/", views.post_like, name='post_like'),
    path("my_posts/<str:u>", views.my_posts, name='my_posts'),
    path("teacher_posts/<str:u>", views.my_posts, name='teacher_posts'),
    path("comment", views.comment, name='comment'),
    path("delete_post", views.delete_post, name='delete_post'),
    path("delete_comment", views.delete_comment, name='delete_comment'),
    path("edit_post/<str:u>", views.edit_post, name='edit_post'),
    path("teacher_edit_post/<str:u>", views.edit_post, name='teacher_edit_post'),
    path("edit_comment", views.edit_comment, name="edit_comment"),
]