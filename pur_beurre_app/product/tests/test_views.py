import pytest

from django.urls import reverse
from django.test import Client
from product.models import Product
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
def test_search_product_view():
    client = Client()
    path = reverse('search-product')
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "product/search_product.html")

@pytest.mark.django_db
def test_favorite_product_view():
    client = Client()
    path = reverse('favorite-product')
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "product/favorite_product.html")
