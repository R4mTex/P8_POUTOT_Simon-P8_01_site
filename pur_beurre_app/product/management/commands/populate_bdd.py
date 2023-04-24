from django.core.management.base import BaseCommand
from product.scripts.downloader import Downloader
from product.models import Product, Category
from django.db import IntegrityError
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Create products'

    def add_arguments(self, parser):
        parser.add_argument('nb_pages', type=int, help='Indicates the number of pages of products to be created')
        parser.add_argument('nb_products', type=int, help='Indicates the number of products to be created')

    def handle(self, *args, **kwargs):
        print("\nStarting Process.\n")

        Product.objects.all().delete()
        print("Products Deleted.")
        Category.objects.all().delete()
        print("""Categories Deleted.\n
Download Products And Categories From OpenFoodFacts In Progress.\n""")

        nb_pages = kwargs['nb_pages']
        nb_products = kwargs['nb_products']

        products_downloaded = Downloader.get_products(nb_pages, nb_products)

        print("\nAdd Products And Categories To The Current Database In Progress.\n")

        for product in tqdm(range(len(products_downloaded))):
            new_category = Category()
            new_category.name = products_downloaded[product]['category']
            new_product = Product()
            new_product.name = str(products_downloaded[product]['name'])
            new_product.description = str(products_downloaded[product]['description'])
            new_product.store = str(products_downloaded[product]['store'])
            new_product.url = products_downloaded[product]['url']
            new_product.img = products_downloaded[product]['img']
            new_product.nutriscore = str(products_downloaded[product]['nutriscore'])
            new_product.nutriments = products_downloaded[product]['nutriments']
            try:
                new_product.save()
                new_category = new_product.category.create(name=new_category.name)
            except IntegrityError:
                continue
        return """\nProducts Added.
Categories Added.\n
Ending Process."""
