from django.urls import path, include
from django.conf.urls.static import static  # imagem
from django.conf import settings
from gerencia.views import home, entradas, produtos, relatorios, saidas, cadastro

urlpatterns = [
    path('', home, name='home'),  # Home
    path('entradas/', entradas, name='entradas'),
    path('produtos/', produtos, name='produtos'),
    path('relatorios/', relatorios, name='relatorios'),
    path('saidas/', saidas, name='saidas'),
    path('cadastro/', cadastro, name='cadastro'),

] + static(settings.MIDIA_URL, document_root=settings.MIDIA_ROOT)
