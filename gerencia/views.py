from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        # Criar um novo objeto Produto com os dados do formulário
        novo_produto = Produtos()
        novo_produto.nome = request.POST.get('nome')
        novo_produto.marca = request.POST.get('marca')
        novo_produto.quantidade = request.POST.get('quantidade')
        novo_produto.descricao = request.POST.get('descricao')
        novo_produto.preco = request.POST.get('preco')
        novo_produto.save()

        # Redirecionar para a página de sucesso ou qualquer outra página desejada
        return redirect('.')

    # Se a requisição não for POST, apenas renderize o formulário
    return render(request, 'gerencia/pages/cadastro.html')

# Se desejar, você pode criar uma página de sucesso após o cadastro
def pagina_sucesso(request):
    return render(request, 'gerencia/pages/entradas.html')