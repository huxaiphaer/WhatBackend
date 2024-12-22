from django.urls import path
from .views import ProductListCreateView, toggle_product_selection

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('select/<uuid:pk>/', toggle_product_selection, name='select-product'),
]
