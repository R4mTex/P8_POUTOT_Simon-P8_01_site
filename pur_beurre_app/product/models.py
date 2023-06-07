from django.db import models
from authentication.models import User

# Create your models here.
class Category(models.Model):
    name = models.fields.TextField(max_length=1024,)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.fields.CharField(max_length=256, unique=True,)
    category = models.ManyToManyField(Category)
    description = models.fields.TextField(max_length=2048, null=True,)
    store = models.fields.TextField(max_length=1024, null=True)
    url = models.URLField(max_length=200,)
    img = models.fields.CharField(max_length=256,)
    nutriscore = models.fields.CharField(max_length=256,)
    nutriments = models.JSONField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='favorites', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user}'
