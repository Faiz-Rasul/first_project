from django.urls import path
from . import views

urlpatterns = [
    path("add_products/", views.add_products, name='add_products'),
    path("all_products", views.all_products, name='all_products'),
    path("my_cart", views.my_cart, name='my_cart'),
    path("my_orders", views.my_orders, name='my_orders'),
    path('increment', views.increment, name='increment'),
    path('decrement', views.decrement, name='decrement'),
    path('empty_cart', views.empty_cart, name='empty_cart')
]