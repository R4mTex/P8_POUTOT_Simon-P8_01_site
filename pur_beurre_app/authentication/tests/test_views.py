import pytest

from django.urls import reverse
from django.test import Client
from django.contrib.auth import login, authenticate 
from authentication.models import User
from pytest_django.asserts import assertTemplateUsed
from authentication import forms 


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
    '''login requirement'''
    User.objects.create_user(username = 'Test User',
                             email = '',
                             password = '',
                             )
    client.login(username='Test User', email='', password='')
    path = reverse('home')
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

    form = forms.LoginForm()
    message = ''

    path = reverse('login',)
    response = client.get(path, context={'form': form, 'message': message})

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/login.html")

@pytest.mark.django_db
def test_post_login_view():
    client = Client()
    
    path = reverse('login',)
    response = client.post(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/login.html")

def test_should_return_true_if_form_is_valid():
    form_data = {'username': 'Test Username', 'password': 'Test Password'}
    form = forms.LoginForm(data=form_data)
    expected_value = True 
    assert form.is_valid() == expected_value

@pytest.mark.django_db  
def test_mentions_legals_view():
    client = Client()

    path = reverse('mentions-legals',)
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "authentication/mentions_legals.html")