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

from django.contrib import admin
from django.urls import path
from authentication import views

import authentication.views

from product.views import search_product, favorite_product, product_detail


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("login/", LoginView.as_view(
                template_name='authentication/login.html',
                redirect_authenticated_user=True),
            name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path("signup/", authentication.views.signup_page, name='signup'),
    path("user-profile/<int:id>/", views.user_profile, name='user-profile'),
    path("product-detail/<int:id>/", product_detail.as_view(
                template_name='product/product_detail.html'), 
            name='product-detail'),
    path("search-product/", search_product.as_view(
                template_name='product/search_product.html'), 
            name='search-product'),
    path("favorite-product/", favorite_product.as_view(
                template_name='product/favorite_product.html'), 
            name='favorite-product'),
    path("mentions-légales/", views.mentions_legals, name='mentions-légales'),
]
