import requests
from tqdm import tqdm
from json import JSONDecodeError


class Downloader:
    def get_products(nb_pages, nb_products):
        data_products = []

        for i in tqdm(range(nb_pages)):
            payload = {
                "action": "process",
                "tagtype_0": "products",
                "tag_contains_0": "contains",
                "page_size": nb_products,
                "page": i + 1,
                "json": "true",
            }
            response_products = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl", params=payload
            )
            try:
                data_json = response_products.json()
            except JSONDecodeError:
                continue
            data_products.extend(data_json.get("products"))

        """save values from products in some lists"""
        products_names = [
            x.get("product_name_fr", "None") for x in data_products
        ]
        products_categories = [
            x.get("categories", "None") for x in data_products
        ]
        products_descriptions = [
            x.get("ingredients_text_fr", "None") for x in data_products
        ]
        products_stores = [x.get("stores", "None") for x in data_products]
        products_urls = [x.get("url", "None") for x in data_products]
        products_imgs_urls = [x.get("image_url", "None") for x in data_products]
        products_nutriscores = [
            x.get("nutriscore_grade", "None") for x in data_products
        ]
        products_nutriments = [
            x.get("nutriments", "None") for x in data_products
        ]

        """append some values in a list from the products structure"""
        products = []
        for x in range(len(data_products)):
            products_structure = {
                "name": products_names[x].lower(),
                "category": [
                    element.strip()
                    for element in products_categories[x].lower().split(",")
                ],
                "description": products_descriptions[x].lower(),
                "store": [
                    element.strip()
                    for element in products_stores[x].lower().split(",")
                ],
                "url": products_urls[x].lower(),
                "img": products_imgs_urls[x].lower(),
                "nutriscore": products_nutriscores[x].lower(),
                "nutriments": products_nutriments[x],
            }
            products.append(products_structure)
        return products
