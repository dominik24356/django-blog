from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # ADMIN ONLY
    # path('create/', views.create_product, name='create_product'),
    # path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    # path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
]