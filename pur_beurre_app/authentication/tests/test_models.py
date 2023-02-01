import pytest

from django.test import Client
from authentication.models import User

@pytest.mark.django_db  
def test_user_model():
    client = Client()
    user = User.objects.create(username = 'Test User',
                               email = '',
                               password = '',
                               )
    expected_value = "Test User"
    assert str(user) == expected_value
