from django.urls import path

import mainapp.views as mainapp
from .views import products, product
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
   path('', products, name='index'),
   path('category/<int:pk>', products, name='category'),
   path('category/<int:pk>/page/<int:page>/', cache_page(3600)(products), name='page'),
   path('category/ajax/', cache_page(3600)(mainapp.products_ajax)),
   path('category/<int:pk>/page/<int:page>/ajax/', cache_page(3600)(mainapp.products_ajax)),
   path('category/<int:pk>', product, name='detail'),
]
