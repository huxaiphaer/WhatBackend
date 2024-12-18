import pytest
from django.urls import reverse
from rest_framework import status

from products.models import Product


@pytest.mark.django_db
def test_create_product(client):
    response = client.post(reverse('product-list-create'), {
        "name": "Test Product",
        "description": "A test product",
        "price": "10.99",
        "stock": 50
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.count() == 1


@pytest.mark.django_db
def test_list_products(client):
    Product.objects.create(name="Product 1", description="Desc 1", price="5.99", stock=10)
    Product.objects.create(name="Product 2", description="Desc 2", price="9.99", stock=20)

    response = client.get(reverse('product-list-create'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


@pytest.mark.django_db
def test_select_product(client):
    product = Product.objects.create(name="Product 1", description="Desc 1", price="5.99", stock=10)
    response = client.post(reverse('select-product', args=[product.id]))
    assert response.status_code == status.HTTP_200_OK
    product.refresh_from_db()
    assert product.selected is True
