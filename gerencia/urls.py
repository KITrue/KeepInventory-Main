from django.urls import path, include
from django.conf.urls.static import static  # imagem
from django.conf import settings
from gerencia.views import home, entradas, relatorios, cadastro, editar, deletar

urlpatterns = [
    path('', home, name='home'),  # Home
    path('gerenciamento/', entradas, name='entradas'),
    path('relatorios/', relatorios, name='relatorios'),
    path('cadastro/', cadastro, name='cadastro'),
    path('editar/<int:id>', editar, name='editar'),
    path('deletar/<int:id>', deletar, name='deletar')

]
