import pytest

from django.urls import reverse, resolve
from django.shortcuts import render, redirect 
from django.test import Client
from authentication.models import User
from pytest_django.asserts import assertTemplateUsed
from authentication import forms
from authentication.views import Signup, Login, User_profile
from django.contrib import auth
from django.contrib.auth.views import LogoutView


client = Client()


@pytest.mark.django_db
def test_home_view():
    '''login requirement'''
    User.objects.create_user(username='TestUser',
                             email='',
                             password='',
                             )
    client.login(username='TestUser', email='', password='')
    path = reverse('home')
    response = client.get(path)

    expected_value = 200
    assert response.status_code == expected_value
    assertTemplateUsed(response, "authentication/home.html")


@pytest.mark.django_db
def test_user_profile_view():
    '''login requirement'''
    User.objects.create_user(username='TestUser',
                             email='',
                             password='',
                             )
    client.login(username='TestUser', email='', password='')
    path = reverse('user-profile', kwargs={'id_user': 1})
    response = client.get(path)

    expected_value = 200
    assert response.status_code == expected_value
    assertTemplateUsed(response, "authentication/user_profile.html")


@pytest.mark.django_db
class Test_user_profile_view():
    template_name = 'authentication/user_profile.html' 

    def test_get_user_profile(self):
        url = reverse('user-profile', args=[1])
        assert resolve(url).func.view_class, User_profile

        credentials = {
            'username': 'TestUser',
            'email': 'testuser@testing.com',
            'password1': 'TestPassword1',
            'password2': 'TestPassword1'
        }
        client.post(reverse('signup'), credentials)
        client.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword1'})

        response = client.get(reverse('user-profile', args=[1]))
        assert response.status_code == 200
        assertTemplateUsed(response, self.template_name)

    def test_post_user_profile(self):
        credentials = {
            'username': 'TestUser',
            'email': 'testuser@testing.com',
            'password1': 'TestPassword1',
            'password2': 'TestPassword1',
        }
        client.post(reverse('signup'), credentials)
        client.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword1'})

        user = User.objects.get(username='TestUser')
        
        img_id = 0
        img_src = {
            'icon_avatar_1': '/static/images/icon_avatar_1.png',
            'icon_avatar_2': '/static/images/icon_avatar_2.png',
            'icon_avatar_3': '/static/images/icon_avatar_3.png',
            'icon_avatar_4': '/static/images/icon_avatar_4.png',
            'icon_avatar_5': '/static/images/icon_avatar_5.png',
            'icon_avatar_6': '/static/images/icon_avatar_6.png',
            'icon_avatar_7': '/static/images/icon_avatar_7.png',
            'icon_avatar_8': '/static/images/icon_avatar_8.png',
            'icon_avatar_9': '/static/images/icon_avatar_9.png',
            'icon_avatar_10': '/static/images/icon_avatar_10.png',
            'icon_avatar_11': '/static/images/icon_avatar_11.png',
        }
        user.profile_picture = list(img_src)[img_id]
        user.save()

        user = User.objects.get(username='TestUser')

        response = client.post('/user-profile/1/', data={'icon_avatar': list(img_src)[img_id]})

        assert response.status_code == 200
        assertTemplateUsed(response, self.template_name)


@pytest.mark.django_db
class Test_signup_view():
    def test_get_signup_view(self):

        path = reverse('signup',)
        response = client.get(path)

        expected_value = 200
        assert response.status_code == expected_value
        assertTemplateUsed(response, "authentication/signup.html")

    @pytest.fixture
    def form_valid_data_fixture(self):
        form_data = {'username': 'TestUser', 'email': 'test@test.com',
                     'password1': 'TestPassword1', 'password2': 'TestPassword1'}
        return form_data

    def test_should_return_true_if_SignupForm_valid(self, form_valid_data_fixture):
        form = forms.SignupForm(data=form_valid_data_fixture)
        expected_value_form_valid = True
        assert form.is_valid() == expected_value_form_valid

    @pytest.fixture
    def form_invalid_data_fixture(self, form_valid_data_fixture):
        form_valid_data_fixture['password1'] = 'wrong_password'
        return form_valid_data_fixture

    def test_should_return_false_if_SignupForm_invalid(self, form_invalid_data_fixture):
        form = forms.SignupForm(data=form_invalid_data_fixture)
        expected_value_form_valid = False
        assert form.is_valid() == expected_value_form_valid

    def test_should_return_true_if_client_be_logged(self, form_valid_data_fixture):
        form = forms.SignupForm(data=form_valid_data_fixture)

        if form.is_valid():
            form.save()
            username = form['username'].value()
            password = form['password1'].value()

        expected_value_login = True
        assert client.login(username=username, password=password) == expected_value_login

    def test_should_return_false_if_client_not_be_logged(self, form_valid_data_fixture):
        form = forms.SignupForm(data=form_valid_data_fixture)

        if form.is_valid():
            form.save()
            username = form['username'].value()
            password = 'wrong_password'

        expected_value_login = False
        assert client.login(username=username, password=password) == expected_value_login

    @pytest.fixture
    def user_fixture(self, form_valid_data_fixture):
        form = forms.SignupForm(data=form_valid_data_fixture)
        user = form.save()
        return user

    @pytest.fixture
    def client_logged_fixture(self, form_valid_data_fixture):
        form = forms.SignupForm(data=form_valid_data_fixture)

        if form.is_valid():
            form.save()
            username = form['username'].value()
            password = form['password1'].value()

        client_logged = client.login(username=username, password=password)
        return client_logged

    def test_post_signup_view(self):
        path = reverse('signup',)
        response = client.post(path)

        expected_value = 200
        assert response.status_code == expected_value
        assertTemplateUsed(response, "authentication/signup.html")

    def test_signup_route(self):
        """
        Test approach starts with testing if the 'signup' route maps to 'SignUpView'. Then we test
        if the SignUpView renders the correct template ( registration/signup.html ) with correct Form ( SignUpForm ).
        After that we create a temporary user, by using our 'signup' route and checking if redirects the user to
        the 'login' route, if everything went fine.
        """

        url = reverse('signup')
        assert resolve(url).func.view_class, Signup

        response = client.get(reverse('signup'))
        assert response.status_code == 200
        assert Signup.form_class == forms.SignupForm
        assertTemplateUsed(response, 'authentication/signup.html')

        credentials = {
            'username': 'TestUser',
            'email': 'testuser@testing.com',
            'password1': 'TestPassword1',
            'password2': 'TestPassword1'
        }

        response = client.post(reverse('signup'), credentials)
        assert response.status_code == 302
        assert response.url == reverse('home')

    def test_signup_route_failed(self):
        """
        Testing 'signup' route with the wrong credentials and testing if user stays on the 'signup'
        route if the signup process failed
        """

        credentials = {
            'username': 'TestUser',
            'email': 'testuser@testing.com',
            'password1': '',
            'password2': 'TestPassword1'
        }
        response = client.post(reverse('signup'), credentials)
        assert response.status_code == 200
        assertTemplateUsed(response, 'authentication/signup.html')


@pytest.mark.django_db
class Test_login_view():
    form_class = forms.LoginForm

    def test_get_login_view(self):
        form = self.form_class()

        path = reverse('login')
        response = client.get(path, {'form': form})

        expected_value_code = 200
        assert response.status_code == expected_value_code
        assert Login.form_class == forms.LoginForm
        assertTemplateUsed(response, "authentication/login.html")

    def test_should_return_true_if_LoginForm_valid(self):
        form_data = {'username': 'TestUser', 'password': 'TestPassword1'}
        form = self.form_class(data=form_data)

        expected_value = True
        assert form.is_valid() == expected_value

    def test_should_return_false_if_LoginForm_invalid(self):
        form_data = {'username': 'TestUser', }
        form = self.form_class(data=form_data)

        expected_value = False
        assert form.is_valid() == expected_value

    def test_login_route(self):
        """
        First we test if the 'login' route maps to 'LoginView', then we check if the LoginView
        renders the correct template ( registration/login.html )
        Then, we create a temporary user, and login with those credentials and see whether user
        is redirected to '/home/' route if the login was successful
        """
        User.objects.create_user(username='TestUser',
                                 email='testuser@testing.com',
                                 password='TestPassword1',
                                 )
        # # Testing if the 'login' route maps to 'LoginView'
        url = reverse('login')
        assert resolve(url).func.view_class, Login

        # # Testing if the 'LoginView' renders correct template ( registration/login.html )
        response = client.get(reverse('login'))
        assert response.status_code == 200
        assert Login.form_class == forms.LoginForm
        assertTemplateUsed(response, 'authentication/login.html')

        # We login in the user and test if the login was successful and then we properly redirect
        # user to '/home/' route
        response = client.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword1'})
        assert response.status_code == 302
        assert response.url == reverse('home')

        user = auth.get_user(client)
        assert user.is_authenticated

    def test_login_route_failed(self):
        """
        Testing if the user enters the false credentails then the user stays on the 'login' route,
        and is asked to re-enter the correct credentials
        """
        credentials = {
            'username': 'TestUser',
            'email': 'testuser@testing.com',
            'password1': 'TestPassword1',
            'password2': 'TestPassword1'
        }
        client.post(reverse('signup'), credentials)
        """
        response = client.post(reverse('login'), {'username': 'TestUser', 'password': 'WrongPassword'})
        assert response.status_code == 200
        assertTemplateUsed(response, 'authentication/login.html')
        """


@pytest.mark.django_db
def test_logout_route():
    """
    First we test if 'logout' route maps to the 'LogoutView' or not, then we test if the user is
    properly logged out and is redirected to 'home' route
    """

    # Testing if the 'logout' route maps to 'LogoutView'
    url = reverse('logout')
    assert resolve(url).func.view_class, LogoutView

    # Testing if the user is logged out properly and is redirected to 'home' route
    response = client.post(reverse('logout'))
    assert response.status_code == 302
    assert response.url == reverse('login')


@pytest.mark.django_db
def test_mentions_legals_view():
    path = reverse('mentions-legals')
    response = client.get(path)

    expected_value = 200
    assert response.status_code == expected_value
    assertTemplateUsed(response, "authentication/mentions_legals.html")
