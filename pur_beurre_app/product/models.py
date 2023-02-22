from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.fields.CharField(max_length=100,)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.fields.CharField(max_length=100, unique=True,)
    category = models.ManyToManyField(Category)
    description = models.fields.TextField(max_length=3000, null=True,)
    store = models.fields.CharField(max_length=100, null=True)
    url = models.URLField(max_length=200,)
    img = models.ImageField(max_length=100,)
    nutriscore = models.fields.CharField(max_length=100,)
    nutriments = models.JSONField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Favorite(models.Model):
    product = models.ForeignKey('Product', related_name='favorites', on_delete=models.CASCADE)

    class Meta:
        ordering = ['product']

    def __str__(self):
        return f'{self.product}'
