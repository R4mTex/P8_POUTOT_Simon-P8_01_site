import pytest

from django.urls import reverse
from django.test import Client
from product.models import Product, Category, Favorite
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_product_detail_view():
    client = Client()
    Product.objects.create(name = 'Test Product',
                           description = '',
                           store = '',
                           url = '',
                           img = '',
                           nutriscore = '',
                           nutriments = {},
                           )
    path = reverse('product-detail', kwargs={'id':1})
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "product/product_detail.html")

@pytest.mark.django_db
def test_get_search_product_view():
    client = Client()
    new_category = Category()
    new_category.name = 'Test Category'
    new_product = Product()
    new_product.name = 'Test Product'
    new_product.description = ''
    new_product.store = ''
    new_product.url = ''
    new_product.img = ''
    new_product.nutriscore = ''
    new_product.nutriments = {}

    new_product.save()
    new_category = new_product.category.create(name=new_category.name)
  
    path = reverse('search-product')
    response = client.get(path, {'question': Product.objects.get(name='Test Product')})

    assert response.status_code == 200
    assertTemplateUsed(response, "product/search_product.html")

@pytest.mark.django_db
def test_get_favorite_product_view():
    client = Client()
    path = reverse('favorite-product')
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "product/favorite_product.html")

"""
@pytest.mark.django_db
def test_post_favorite_product_view():
    client = Client()
    product = Product.objects.create(name = 'Test Product',
                                      description = '',
                                      store = '',
                                      url = '',
                                      img = '',
                                      nutriscore = '',
                                      nutriments = {},
                                      )
    favorite = Favorite.objects.create(product=Product.objects.get(id=1))
    favorite_id = Favorite.objects.get(id=1).id

    path = reverse('favorite-product')
    response = client.post(path, {'favorite_id': favorite_id})

    assert response.status_code == 200
    assertTemplateUsed(response, "product/favorite_product.html")
"""
