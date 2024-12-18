import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_signup(client):
    response = client.post(reverse('signup'), {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_signup_with_existing_username(client, create_test_user):
    response = client.post(reverse('signup'), {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['error'] == 'Username already exists'


@pytest.mark.django_db
def test_login(client, create_test_user):
    response = client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_login_with_invalid_credentials(client):
    response = client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'wrongpassword'
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data['error'] == 'Invalid credentials'
