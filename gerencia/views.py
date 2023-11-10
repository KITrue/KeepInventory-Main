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


def lte(request):
    return render(request, 'adminlte/starter.html')


def entradas(request):
    produtos = Produtos.objects.all()
    return render(request, 'gerencia/pages/entradas.html', {'produtos': produtos})


def relatorios(request):
    return render(request, 'gerencia/pages/relatorios.html')


# ----------------------------------- API - Cadastrar ----------------------------------- #


def cadastro(request):
    if request.method == 'POST':
        # Criar um novo objeto Produto com os dados do formulário
        novo_produto = Produtos()
        novo_produto.nome = request.POST.get('nome')
        novo_produto.marca = request.POST.get('marca')
        novo_produto.quantidade = request.POST.get('quantidade')
        novo_produto.descricao = request.POST.get('descricao')
        novo_produto.preco = request.POST.get('preco')
        novo_produto.imagem = request.FILES.get('imagem')
        novo_produto.save()

        # Redirecionar para a página de sucesso ou qualquer outra página desejada
        return redirect('entradas')

    # Se a requisição não for POST, apenas renderize o formulário
    return render(request, 'gerencia/pages/cadastro.html')

# Se desejar, você pode criar uma página de sucesso após o cadastro


def pagina_sucesso(request):
    return render(request, 'gerencia/pages/entradas.html')

# ----------------------------------- API - Excluir ----------------------------------- #


def deletar(request, id):
    delete_produtos = Produtos.objects.get(id=id)
    delete_produtos.delete()
    return redirect('entradas')


# ----------------------------------- API - Editar ----------------------------------- #

# def editar(request, id):
#     editar_produto = Produtos.objects.get(id=id)
#     return render(request, {"produtos": editar_produto})


def editar(request, id):
    if request.method == 'POST':
        produto = Produtos.objects.get(id=id)

        vnome = request.POST.get('nome')
        produto.nome = vnome

        vmarca = request.POST.get('marca')
        produto.marca = vmarca

        vquantidade = request.POST.get('quantidade')
        produto.quantidade = vquantidade

        vdescricao = request.POST.get('descricao')
        produto.descricao = vdescricao

        vpreco = request.POST.get('preco')
        produto.preco = vpreco

        # vimagem = request.FILES.get('imagem')

        produto.save()

    return redirect('entradas')
