from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('product_create/', views.product_create_view, name='product_add'),
    path('product_update/<int:pk>', views.product_update_view, name='product_update'),
    path('confirm_delete/<int:pk>', views.confirm_delete_view, name='confirm_delete'),
    path('product_delete/<int:pk>', views.product_delete_view, name='product_delete'),
]
