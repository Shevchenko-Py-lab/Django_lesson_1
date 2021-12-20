from django.shortcuts import render
from mainapp.models import Product

# Create your views here.


def products(request):
    title = 'каталог'
    links_menu = [
        {'href': 'products/', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    # product = Product.objects.get(id=pk)

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=context)
