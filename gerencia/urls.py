from django.urls import path, include
from django.conf.urls.static import static  # imagem
from django.conf import settings                                                                 
from gerencia.views import home, entradas, relatorios, cadastro, editar, deletar, lte, adicionar, retirar, export_excl, get_product_data

urlpatterns = [
    path('', home, name='home'),  # Home
    path('gerenciamento/', entradas, name='entradas'),
    path('relatorios/', relatorios, name='relatorios'),
    path('cadastro/', cadastro, name='cadastro'),
    path('editar/<int:id>', editar, name='editar'),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('adicionar/<int:id>', adicionar, name='adicionar'),
    path('retirar/<int:id>', retirar, name='retirar'),
    path('export_excl/', export_excl, name='export_excl'),
    path('lte/', lte, name='lte'),
    path('get_product_data/', get_product_data, name='get_product_data'),
]
