import pytest

from django.urls import reverse, resolve
from django.test import Client
from product.models import Product, Category
from authentication.models import User
from product.models import Favorite
from pytest_django.asserts import assertTemplateUsed
from product.views import Favorite_product


@pytest.mark.django_db
def test_get_product_detail_view():
    client = Client()
    '''login requirement'''
    User.objects.create_user(username='TestUser',
                             email='',
                             password='',
                             )
    client.login(username='TestUser', email='', password='')

    Product.objects.create(name='TestProduct',
                           description='',
                           store='',
                           url='',
                           img='',
                           nutriscore='',
                           nutriments={},
                           )

    path = reverse('product-detail', kwargs={'id_user': 1, 'id': 1})
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "product/product_detail.html")


@pytest.mark.django_db
def test_post_product_detail_view():
    client = Client()
    '''login requirement'''
    User.objects.create_user(username='TestUser',
                             email='',
                             password='',
                             )
    client.login(username='TestUser', email='', password='')

    new_category = Category()
    new_category.name = 'TestCategory'
    new_product = Product()
    new_product.name = 'TestProduct'
    new_product.description = ''
    new_product.store = ''
    new_product.url = ''
    new_product.img = ''
    new_product.nutriscore = ''
    new_product.nutriments = {}

    new_product.save()
    new_category = new_product.category.create(name=new_category.name)

    path = reverse('product-detail', kwargs={'id_user': 1, 'id': 1})
    response = client.post(path)

    assert response.status_code == 302
    assert response.url == reverse('favorite-product', kwargs={'id_user': 1})

# -------------------------------------------------------------------------------------------- #

@pytest.mark.django_db
class Test_search_product_view():
    def test_get_search_product(self):
        client = Client()
        '''login requirement'''
        User.objects.create_user(username='TestUser',
                                email='',
                                password='',
                                )
        client.login(username='TestUser', email='', password='')

        new_category = Category()
        new_category.name = 'TestCategory'
        new_product = Product()
        new_product.name = 'TestProduct'
        new_product.description = ''
        new_product.store = ''
        new_product.url = ''
        new_product.img = ''
        new_product.nutriscore = ''
        new_product.nutriments = {}

        new_product.save()
        new_category = new_product.category.create(name=new_category.name)

        path = reverse('search-product', kwargs={'id_user': 1})
        response = client.get(path, {'question': Product.objects.get(name='TestProduct')})

        assert response.status_code == 200
        assertTemplateUsed(response, "product/search_product.html")

    def test_post_search_product(self):
        client = Client()
        '''login requirement'''
        User.objects.create_user(username='TestUser',
                                 email='',
                                 password='',
                                 )
        client.login(username='TestUser', email='', password='')

        new_category = Category()
        new_category.name = 'TestCategory'
        new_product = Product()
        new_product.name = 'TestProduct'
        new_product.description = ''
        new_product.store = ''
        new_product.url = ''
        new_product.img = ''
        new_product.nutriscore = ''
        new_product.nutriments = {}

        new_product.save()
        new_category = new_product.category.create(name=new_category.name)

        path = reverse('search-product', kwargs={'id_user': 1})
        response = client.post(path, data={'submit': 1})

        assert response.status_code == 302
        assert response.url == reverse('favorite-product', kwargs={'id_user': 1})

# -------------------------------------------------------------------------------------------- #


@pytest.mark.django_db
def test_get_favorite_product_view():
    client = Client()
    '''login requirement'''
    User.objects.create_user(username='Test User',
                             email='',
                             password='',
                             )
    client.login(username='Test User', email='', password='')
    path = reverse('favorite-product', kwargs={'id_user': 1})
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "product/favorite_product.html")


@pytest.mark.django_db
def test_post_favorite_product_view():
    client = Client()
    '''login requirement'''
    User.objects.create_user(username='TestUser',
                             email='',
                             password='',
                             )
    client.login(username='TestUser', email='', password='')

    new_category = Category()
    new_category.name = 'TestCategory'
    new_product = Product()
    new_product.name = 'TestProduct'
    new_product.description = ''
    new_product.store = ''
    new_product.url = ''
    new_product.img = ''
    new_product.nutriscore = ''
    new_product.nutriments = {}

    new_product.save()
    new_category = new_product.category.create(name=new_category.name)

    path = reverse('favorite-product', kwargs={'id_user': 1})
    response = client.post(path, data={'submit': 1})

    assert response.status_code == 200


@pytest.mark.django_db
def test_favorite_route():
    client = Client()
    '''login requirement'''
    User.objects.create_user(username='Test User',
                             email='',
                             password='',
                             )
    client.login(username='Test User', email='', password='')

    url = reverse('favorite-product', kwargs={'id_user': 1})
    assert resolve(url).func.view_class, Favorite_product

    response = client.get(reverse('favorite-product', kwargs={'id_user': 1}))
    assert response.status_code == 200
    assertTemplateUsed(response, 'product/favorite_product.html')

# -------------------------------------------------------------------------------------------- #
