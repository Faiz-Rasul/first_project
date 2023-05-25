from django.urls import path
from . import views

urlpatterns = [
    path("add_products/", views.add_products, name='add_products'),
    path("all_products", views.all_products, name='all_products'),
    path("my_cart", views.my_cart, name='my_cart'),
    path("my_orders", views.my_orders, name='my_orders'),
    path('increment', views.increment, name='increment'),
    path('decrement', views.decrement, name='decrement'),
    path('empty_cart', views.empty_cart, name='empty_cart'),
    path('search_product', views.search_product, name='search_product'),
]


htmx_urlpatterns = [
    path("add_to_cart_htmx", views.add_to_cart_htmx, name='add_to_cart_htmx'),
    path("clear", views.clear, name='clear'),
    path("delete_from_cart", views.delete_from_cart, name='delete_from_cart'),
]

urlpatterns += htmx_urlpatterns