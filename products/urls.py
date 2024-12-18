from django.urls import path
from .views import ProductListCreateView, select_product

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('select/<uuid:pk>/', select_product, name='select-product'),
]
