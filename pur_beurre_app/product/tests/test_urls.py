import pytest
from django.urls import reverse, resolve


@pytest.mark.django_db
def test_product_detail_url():
    path = reverse('product-detail', kwargs={'id_user': 1, 'id': 1})

    assert path == "/product-detail/1/1/"
    assert resolve(path).view_name == "product-detail"


@pytest.mark.django_db
def test_search_product_url():
    path = reverse('search-product', kwargs={'id_user': 1})

    assert path == "/search-product/1/"
    assert resolve(path).view_name == "search-product"


@pytest.mark.django_db
def test_favorite_product_url():
    path = reverse('favorite-product', kwargs={'id_user': 1})

    assert path == "/favorite-product/1/"
    assert resolve(path).view_name == "favorite-product"
