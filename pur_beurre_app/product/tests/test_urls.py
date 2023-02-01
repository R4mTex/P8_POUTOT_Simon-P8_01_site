import pytest

from django.urls import reverse, resolve
from product.models import Product

@pytest.mark.django_db
def test_product_detail_url():
    Product.objects.create(name = '',
                           description = '',
                           store = '',
                           url = '',
                           img = '',
                           nutriscore = '',
                           nutriments = {},
                           )
    path = reverse('product-detail', kwargs={'id':1})

    assert path == "/product-detail/1/"
    assert resolve(path).view_name == "product-detail"

@pytest.mark.django_db
def test_search_product_url():
    path = reverse('search-product')

    assert path == "/search-product/"
    assert resolve(path).view_name == "search-product"

@pytest.mark.django_db
def test_favorite_product_url():
    path = reverse('favorite-product')

    assert path == "/favorite-product/"
    assert resolve(path).view_name == "favorite-product"
