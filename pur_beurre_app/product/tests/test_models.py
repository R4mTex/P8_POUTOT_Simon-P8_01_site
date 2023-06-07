import pytest
from authentication.models import User
from product.models import Product, Category, Favorite


@pytest.mark.django_db
def test_product_model():
    product = Product.objects.create(name='Test Product',
                                     description='',
                                     store='',
                                     url='',
                                     img='',
                                     nutriscore='',
                                     nutriments={},
                                     )

    expected_value = 'Test Product'
    assert str(product) == expected_value


@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(name='Test Category',)

    expected_value = 'Test Category'
    assert str(category) == expected_value


@pytest.mark.django_db
def test_favorite_model():
    User.objects.create(username='Test',
                        password='Test1test1',
                        email='test@test.com')
    Product.objects.create(name='Test Product/Favorite',
                           description='',
                           store='',
                           url='',
                           img='',
                           nutriscore='',
                           nutriments={},
                           )
    favorite = Favorite.objects.create(product=Product.objects.get(name='Test Product/Favorite'), user=User.objects.get(username='Test'))

    expected_value = 'Test'
    assert str(favorite) == expected_value
