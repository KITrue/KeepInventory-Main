from django.shortcuts import render
from rest_framework import viewsets
from .models import Produtos
from .api.serializers import ProdutosSerializer

# from django.http import HttpResponse


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer


def home(request):
    return render(request, 'gerencia/pages/home.html')


def entradas(request):
    return render(request, 'gerencia/pages/entradas.html')


def produtos(request):
    return render(request, 'gerencia/pages/produtos.html')


def relatorios(request):
    return render(request, 'gerencia/pages/relatorios.html')


def saidas(request):
    return render(request, 'gerencia/pages/saidas.html')
    

def cadastro(request):
    return render(request, 'gerencia/pages/cadastro.html')
    novo_produto = Produtos()
    # Salvando novo produto para banco de dados
    
    novo_produto.nome = request.POST('nome')
    novo_produto.marca = request.POST('marca')
    novo_produto.total = request.POST('total')
    novo_produto.descricao = request.POST('descricao')
    novo_produto.preco = request.POST('preco')
    novo_produto.save()

    #exibir todos os usuariosjá cadastrados em uma nova página
    produtos = {
        'produtos': Produtos.objects.all()
    
    }
    return render(request, 'gerencia/pages/cadastro.html', produtos)
    

