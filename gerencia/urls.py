from django.urls import path, include

from gerencia.views import home, entradas, produtos, relatorios, saidas, cadastro

urlpatterns = [
    path('', home, name='home'),  # Home
    path('entradas/', entradas, name='entradas'),
    path('produtos/', produtos, name='produtos'),
    path('relatorios/', relatorios, name='relatorios'),
    path('saidas/', saidas, name='saidas'),
    path('cadastro/', cadastro, name='cadastro'),
]
