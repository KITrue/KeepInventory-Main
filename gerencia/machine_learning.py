from django.shortcuts import render
from django.http import JsonResponse
from .models import Produtos, LogEstoque


def chart_data(request):
    produtos = Produtos.objects.all()
    
    labels = [produto.data_entrada.strftime('%Y%m%d') for produto in produtos] # x
    print(labels)
    data = [produto.quantidade for produto in produtos] # y
    
    # Use um atributo específico do seu modelo para calcular o tamanho da bolha
    bubble_size = [produto.quantidade for produto in produtos]

    chart_data = {
        'labels': labels,
        'data': [{'x': x, 'y': y, 'bubbleSize': size} for x, y, size in zip(labels, data, bubble_size)],
    }

    return JsonResponse(chart_data)
