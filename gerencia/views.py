import csv
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from .models import Produtos, LogEstoque
from .api.serializers import ProdutosSerializer
from django.http import HttpResponseBadRequest, HttpResponse
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from random import randint



# from django.http import HttpResponse


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer


def home(request):
    produtos = Produtos.objects.all()
    return render(request, 'gerencia/pages/home.html', {'produtos': produtos})


def entradas(request):
    produtos = Produtos.objects.all()
    return render(request, 'gerencia/pages/entradas.html', {'produtos': produtos})


def relatorios(request):
    ultimo_mes = timezone.now() - timedelta(days=30)
    registros = LogEstoque.objects.filter(data_movimentacao__gte=ultimo_mes).order_by('-data_movimentacao')
    return render(request, 'gerencia/pages/relatorios.html', {'registros': registros})

def test(request):
    produtos = Produtos.objects.all()
    return render(request, 'gerencia/pages/test.html', {'produtos': produtos})

    

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
    # delete_produtos.delete()
    delete_produtos.quantidade = 0
    delete_produtos.data_saida = datetime.now()
    delete_produtos.save()
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


# ----------------------------------- API - Adicionar e retirar ----------------------------------- #


def adicionar(request, id):
    
    produto = get_object_or_404(Produtos, id=id)
    logproduto = LogEstoque(produto_id=id)

    vquantidade = request.POST.get('add_value')
    vquantidade = int(vquantidade)

    if vquantidade < 0:
        return HttpResponseBadRequest("A quantidade não pode ser negativa.")

    produto.quantidade += vquantidade

    logproduto.tipo = 'Entrada'
    logproduto.quantidade = vquantidade

    produto.save()
    logproduto.save()

    return redirect('entradas')
        
        
def retirar(request, id):
    produto = get_object_or_404(Produtos, id=id)
    logproduto = LogEstoque(produto_id=id)

    vquantidade = request.POST.get('ret_value')
    vquantidade = int(vquantidade)

    if vquantidade < 0:
        return HttpResponseBadRequest("A quantidade não pode ser negativa.")

    if vquantidade > produto.quantidade:
        return HttpResponseBadRequest("A quantidade a ser retirada é maior do que a quantidade disponível.")

    produto.quantidade -= vquantidade

    logproduto.tipo = 'Saida'
    logproduto.quantidade = vquantidade

    produto.save()
    logproduto.save()

    return redirect('entradas')
    
# ----------------------------------- API - Exportação do Excel - LOG ----------------------------------- #


def export_excl(request):
    ultimo_mes = timezone.now() - timedelta(days=30)
    registros = LogEstoque.objects.filter(data_movimentacao__gte=ultimo_mes).order_by('-data_movimentacao')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registros.csv"'

    writer = csv.writer(response)
    writer.writerow(['Id_Produto', 'Produto', 'Quantidade', 'Tipo', 'Data de Movimentação'])

    for registro in registros:
        writer.writerow([registro.produto, registro.produto.nome, registro.quantidade, registro.tipo, registro.data_movimentacao])

    return response

# ----------------------------------- Logica grafico ----------------------------------- #

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 dataset to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()

def my_view(request):
    data = {
        'message': 'Hello, world!'
    }
    return JsonResponse(data)


def get_product_data(request):

    queryset = Produtos.objects.values('data_entrada', 'quantidade').order_by('-data_entrada')

    labels = [Produtos.data_entrada for Produtos in queryset]
    dados = [Produtos.quantidade for Produtos in queryset]
    return JsonResponse({'labels': labels, 'data': dados})

    context = {
        'labels': labels,
        'dados': dados,
    }
    return render (request, 'gerencia/partials/graph.html', {'labels': labels, 'dados': dados})
    

def chart_view(request):
    return render(request, 'chartapp/chart.html')


# def funciona_chart(request):
#     labels = [produto.data_entrada for produto in Produtos.objects.all()]
#     data = [produto.quantidade for produto in Produtos.objects.all()]

#     queryset = Produtos.objects.order_by('-population')[:5]
#     for Produtos in queryset:
#         labels.append(Produtos.nome)
#         data.append(Produtos.data_entrada)

#     return render(request, 'graph.html', {
#         'labels': labels,
#         'data': data,
#     })
