from django.shortcuts import render
from django.http import JsonResponse
from .models import Produtos

def chart_data(request):
    produtos = Produtos.objects.all()
    
    datasets = []

    for produto in produtos:
        dataset = {
            'label': produto.nome,
            'data': [{
                'x': produto.data_entrada.strftime('%Y%m%d'),  # Posição X baseada na data
                'y': produto.quantidade,  # Posição Y baseada na quantidade
                'r': produto.quantidade  # Tamanho da bolha baseado no preço
            }],
            'backgroundColor': 'rgba(75, 192, 192, 0.2)',
            'borderColor': 'rgba(75, 192, 192, 1)',
            'borderWidth': 1,
        }

        datasets.append(dataset)

    chart_data = {
        'datasets': datasets,
    }

    return JsonResponse(chart_data)
