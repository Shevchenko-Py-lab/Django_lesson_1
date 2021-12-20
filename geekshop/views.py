from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'Магазин GeekShop'
    products = Product.objects.all()[:3]

    links_menu = [
        {'href': 'index/', 'name': 'домой'},
        {'href': 'products/', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
    ]

    context = {
        'title': title,
        'products': products,
        'links_menu': links_menu,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request, 'geekshop/contacts.html', context=context)

