from django.urls import path
from .views import products, product
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', products, name='index'),
   path('category/<int:pk>', products, name='category'),
   path('category/<int:pk>', product, name='detail'),
   # path('<int:pk>/', products, name='category'),
]