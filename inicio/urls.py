from django.urls import path #Esto llama al archivo settings para django
from inicio.views import inicio

app_name='inicio'

urlpatterns = [
    path('', inicio, name='inicio')
]