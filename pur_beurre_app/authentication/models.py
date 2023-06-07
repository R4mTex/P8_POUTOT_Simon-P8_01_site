from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.fields.EmailField(max_length=256, unique=True)
    profile_picture = models.ImageField(default='/static/images/logo_user.png', upload_to='Avatar')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.username}'
