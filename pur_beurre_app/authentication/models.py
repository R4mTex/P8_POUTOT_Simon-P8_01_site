from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.fields.EmailField(unique=True)

    def __str__(self):
        return f'{self.name}'
