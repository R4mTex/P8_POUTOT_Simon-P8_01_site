import pytest
from django.urls import reverse, resolve
from authentication.models import User


@pytest.mark.django_db
def test_user_profile_url():
    User.objects.create(username='Test User',
                        email='',
                        password='',
                        )
    path = reverse('user-profile', kwargs={'id_user': 1})

    assert path == "/user-profile/1/"
    assert resolve(path).view_name == "user-profile"


@pytest.mark.django_db
def test_home_url():
    path = reverse('home',)

    assert path == "/"
    assert resolve(path).view_name == "home"


@pytest.mark.django_db
def test_login_url():
    path = reverse('login',)

    assert path == "/login/"
    assert resolve(path).view_name == "login"


@pytest.mark.django_db
def test_logout_url():
    path = reverse('logout',)

    assert path == "/logout/"
    assert resolve(path).view_name == "logout"


@pytest.mark.django_db
def test_signup_url():
    path = reverse('signup',)

    assert path == "/signup/"
    assert resolve(path).view_name == "signup"


@pytest.mark.django_db
def test_mentions_legals_url():
    path = reverse('mentions-legals',)

    assert path == "/mentions-legals/"
    assert resolve(path).view_name == "mentions-legals"
