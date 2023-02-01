import pytest

from django.urls import reverse
from django.test import Client
from authentication.models import User
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db  
def test_user_profile_view():
    client = Client()
    User.objects.create(username = 'Test User',
                        email = '',
                        password = '',
                        )
    path = reverse('user-profile', kwargs={'id':1})
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/user_profile.html")

@pytest.mark.django_db  
def test_home_view():
    client = Client()

    path = reverse('home',)
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/home.html")

@pytest.mark.django_db  
def test_get_signup_view():
    client = Client()

    path = reverse('signup',)
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/signup.html")

@pytest.mark.django_db  
def test_post_signup_view():
    client = Client()

    path = reverse('signup',)
    response = client.post(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/signup.html")

@pytest.mark.django_db  
def test_get_login_view():
    client = Client()

    path = reverse('login',)
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/login.html")

@pytest.mark.django_db  
def test_post_login_view():
    client = Client()

    path = reverse('login',)
    response = client.post(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/login.html")

@pytest.mark.django_db  
def test_mentions_legals_view():
    client = Client()

    path = reverse('mentions-legals',)
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/mentions_legals.html")