from django.shortcuts import render
# from django.http import HttpResponse


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
