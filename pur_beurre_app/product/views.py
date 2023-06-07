import random
from django.shortcuts import render, redirect
from django.views.generic import View
from product.models import Product, Favorite
from product.scripts.parser import Parser
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.models import User
from django.urls import reverse



# Create your views here.
class Search_product(LoginRequiredMixin, View):
    template_name = 'product/search_product.html'

    def get(self, request, id_user):
        question = request.GET.get('question', '')
        question_parsed = Parser.parse(question)

        products = Product.objects.all()

        products_names = Product.objects.values_list('name')
        products_names_parsed = []
        for product_name in range(len(products_names)):
            products_names_parsed.append(Parser.parse(products_names[product_name]))

        if question_parsed in products_names_parsed:
            for product in range(len(products)):
                if question_parsed == Parser.parse(products[product].name):
                    product_values = {
                        'id': products[product].id,
                        'name': products[product].name,
                        'category': products[product].category.all()[0].name,
                        'url': products[product].url,
                        'img': products[product].img,
                        'nutriscore': products[product].nutriscore,
                    }
                    substitutes = []
                    for product in range(len(products)):
                        try:
                            if ((product_values['nutriscore'] > products[product].nutriscore
                                or product_values['nutriscore'] == 'a')
                                and product_values['name'] != products[product].name
                                    and product_values['category'] == products[product].category.all()[0].name):
                                substitute = {
                                    'id': products[product].id,
                                    'name': products[product].name,
                                    'category': products[product].category.all()[0].name,
                                    'url': products[product].url,
                                    'img': products[product].img,
                                    'nutriscore': products[product].nutriscore,
                                }
                                substitutes.append(substitute)
                        except IndexError:
                            continue

            if len(substitutes) > 6:
                substitutes = random.sample(substitutes, 6)
            return render(request, self.template_name, context={'product': product_values,
                                                                'substitutes': substitutes, })
        else:
            return redirect('home')

    def post(self, request, id_user):
        substitute_id = request.POST.get("submit")
        save_product = Product.objects.get(id=substitute_id)

        user_favorites = Favorite.objects.filter(user=id_user)

        favorites_names = []
        for favorite in range(len(user_favorites)):
            favorites_names.append(user_favorites[favorite].product.name)

        if save_product.name not in favorites_names:
            new_favorite = Favorite()
            new_favorite.product = save_product
            new_favorite.user = User.objects.get(id=id_user)
            new_favorite.save()

            user_favorites = Favorite.objects.filter(user=id_user)

            all_favorites = []
            for favorite in range(len(user_favorites)):
                all_favorites.append(user_favorites[favorite].product)

            favorites = []
            for favorite in range(len(all_favorites)):
                favorite_product = {
                    'id': all_favorites[favorite].id,
                    'name': all_favorites[favorite].name,
                    'category': str(all_favorites[favorite].category.all()[0]),
                    'url': all_favorites[favorite].url,
                    'img': all_favorites[favorite].img,
                    'nutriscore': all_favorites[favorite].nutriscore,
                }
                favorites.append(favorite_product)
        return redirect(reverse('favorite-product', kwargs={'id_user': id_user}))


class Product_detail(LoginRequiredMixin, View):
    template_name = 'product/product_detail.html'

    def get(self, request, id_user, id):
        product_detail = Product.objects.get(id=id)
        product_detail_nutriments = product_detail.nutriments
        nutriments = {
            'energy_kj_100g': product_detail_nutriments.get('energy-kj_100g', None),
            'energy_kcal_100g': product_detail_nutriments.get('energy-kcal_100g', None),
            'fat_100g': product_detail_nutriments.get('fat_100g', None),
            'saturated_fat_100g': product_detail_nutriments.get('saturated-fat_100g', None),
            'carbohydrates_100g': product_detail_nutriments.get('carbohydrates_100g', None),
            'sugars_100g': product_detail_nutriments.get('sugars_100g', None),
            'fiber_100g': product_detail_nutriments.get('fiber_100g', None),
            'proteins_100g': product_detail_nutriments.get('proteins_100g', None),
            'salt_100g': product_detail_nutriments.get('salt_100g', None),
            'alcohol_100g': product_detail_nutriments.get('alcohol_100g', None),
            'fruits_vegetables_nuts_estimate_from_ingredients_100g':
            product_detail_nutriments.get('fruits-vegetables-nuts-estimate-from-ingredients_100g', None),
        }
        return render(request, self.template_name, {'product_detail': product_detail, 'nutriments': nutriments})

    def post(self, request, id_user, id):
        save_product = Product.objects.get(id=id)
        
        user_favorites = Favorite.objects.filter(user=id_user)

        favorites_names = []
        for favorite in range(len(user_favorites)):
            favorites_names.append(user_favorites[favorite].product.name)

        if save_product.name not in favorites_names:
            new_favorite = Favorite()
            new_favorite.product = save_product
            new_favorite.user = User.objects.get(id=id_user)
            new_favorite.save()

        user_favorites = Favorite.objects.filter(user=id_user)

        all_favorites = []
        for favorite in range(len(user_favorites)):
            all_favorites.append(user_favorites[favorite].product)

        favorites = []
        for favorite in range(len(all_favorites)):
            favorite_product = {
                'id': all_favorites[favorite].id,
                'name': all_favorites[favorite].name,
                'category': str(all_favorites[favorite].category.all()[0]),
                'url': all_favorites[favorite].url,
                'img': all_favorites[favorite].img,
                'nutriscore': all_favorites[favorite].nutriscore,
            }
            favorites.append(favorite_product)
        return redirect(reverse('favorite-product', kwargs={'id_user': id_user}))


class Favorite_product(LoginRequiredMixin, View):
    template_name = 'product/favorite_product.html'

    def get(self, request, id_user):
        user_favorites = Favorite.objects.filter(user=id_user)

        all_favorites = []
        for favorite in range(len(user_favorites)):
            all_favorites.append(user_favorites[favorite].product)

        favorites = []
        for favorite in range(len(all_favorites)):
            favorite_product = {
                'id': all_favorites[favorite].id,
                'name': all_favorites[favorite].name,
                'category': str(all_favorites[favorite].category.all()[0]),
                'url': all_favorites[favorite].url,
                'img': all_favorites[favorite].img,
                'nutriscore': all_favorites[favorite].nutriscore,
            }
            favorites.append(favorite_product)

        if len(favorites) > 6:
            favorites = random.sample(favorites, 6)
        return render(request, self.template_name, context={'favorites': favorites, })

    def post(self, request, id_user):
        favorite_id = int(request.POST.get("submit"))

        user_favorites = Favorite.objects.filter(user=id_user)

        for favorite in range(len(user_favorites)):
            if user_favorites[favorite].product.id == favorite_id:
                Favorite.objects.filter(id=user_favorites[favorite].id).delete()

        user_favorites = Favorite.objects.filter(user=id_user)

        all_favorites = []
        for favorite in range(len(user_favorites)):
            all_favorites.append(user_favorites[favorite].product)

        favorites = []
        for favorite in range(len(all_favorites)):
            favorite_product = {
                'id': all_favorites[favorite].id,
                'name': all_favorites[favorite].name,
                'category': str(all_favorites[favorite].category.all()[0]),
                'url': all_favorites[favorite].url,
                'img': all_favorites[favorite].img,
                'nutriscore': all_favorites[favorite].nutriscore,
            }
            favorites.append(favorite_product)
        return render(request, self.template_name, context={'favorites': favorites, })
