from django.urls import path, include
from django.conf.urls.static import static  # imagem
from django.conf import settings
from gerencia.views import home, entradas, relatorios, cadastro

urlpatterns = [
    path('', home, name='home'),  # Home
    path('entradas/', entradas, name='entradas'),
    path('relatorios/', relatorios, name='relatorios'),
    path('cadastro/', cadastro, name='cadastro'),

]
