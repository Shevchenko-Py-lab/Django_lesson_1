from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    title = 'Магазин GeekShop'
    products = Product.objects.all()[:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    links_menu = [
        {'href': 'index/', 'name': 'домой'},
        {'href': 'products/', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
        {'href': 'basket', 'name': 'корзина'},
    ]

    context = {
        'title': title,
        'products': products,
        'links_menu': links_menu,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'geekshop/contacts.html', context=context)

