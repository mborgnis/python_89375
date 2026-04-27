from django.urls import path #Esto llama al archivo settings > urls
from inicio.views import inicio, productos #Esto llama a la funcion que esta en inicio > views

app_name='inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
]