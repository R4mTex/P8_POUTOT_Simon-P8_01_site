"""pur_beurre_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

import authentication.views
import product.views


urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("", authentication.views.home, name='home'),

    path("login/", LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("signup/", authentication.views.Signup.as_view(
        template_name='authentication/signup.html'),
        name='signup'),
    path("user-profile/<int:id_user>/", authentication.views.User_profile.as_view(
        template_name='authentication/user_profile.html'),
        name='user-profile'),

    path("product-detail/<int:id_user>/<int:id>/", product.views.Product_detail.as_view(
        template_name='product/product_detail.html'),
        name='product-detail'),
    path("search-product/<int:id_user>/", product.views.Search_product.as_view(
        template_name='product/search_product.html'),
        name='search-product'),
    path("favorite-product/<int:id_user>/", product.views.Favorite_product.as_view(
        template_name='product/favorite_product.html'),
        name='favorite-product'),

    path("mentions-legals/", authentication.views.mentions_legals, name='mentions-legals'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
