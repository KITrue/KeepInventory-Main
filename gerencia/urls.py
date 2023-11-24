from django.urls import path, include
from django.conf.urls.static import static  # imagem
from django.conf import settings                                                                 
from gerencia.views import home, entradas, relatorios, cadastro, editar, deletar, lte, adicionar, retirar, LogEstoqueView

urlpatterns = [
    path('', home, name='home'),  # Home
    path('gerenciamento/', entradas, name='entradas'),
    path('relatorios/', relatorios, name='relatorios'),
    path('cadastro/', cadastro, name='cadastro'),
    path('editar/<int:id>', editar, name='editar'),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('adicionar/<int:id>', adicionar, name='adicionar'),
    path('retirar/<int:id>', retirar, name='retirar'),
    path('log-estoque/', LogEstoqueView.as_view(), name='log_estoque'),
    path('lte/', lte, name='lte'),
]
