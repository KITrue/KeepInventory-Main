from rest_framework import serializers
from core.models import produto

class produtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = ['id', 'nome', 'marca', 'quantidade']