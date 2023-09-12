from django.shortcuts import render
from rest_framework import viewsets
from .models import produto
from api.serializers import produtoSerializer

class produtoViewSet(viewsets.ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = produtoSerializer