from django.http import JsonResponse
from django.views import View
from django.db.models import F, Sum, Case, When, Value
from django.db.models.functions import TruncDate
from .models import Produtos, LogEstoque

class ChartDataView(View):
    def get(self, request, *args, **kwargs):
        # Realiza a junção de Produtos e LogEstoque usando annotate para calcular a soma da quantidade
        produtos_queryset = Produtos.objects.annotate(
            data_e_quantidade=F('data_entrada'),
            quantidade_total=F('quantidade')
        ).values('id', 'nome', 'data_e_quantidade', 'quantidade_total')

        log_queryset = LogEstoque.objects.annotate(
            data_e_quantidade=F('data_movimentacao'),
            quantidade_total=F('quantidade')
        ).values('produto__id', 'produto__nome', 'data_e_quantidade', 'quantidade_total', 'tipo')

        # Combina os resultados de Produtos e LogEstoque
        combined_queryset = list(produtos_queryset) + list(log_queryset)

        # Ordena a lista combinada pelo ID do produto e pela data
        combined_queryset.sort(key=lambda x: (x.get('id', x.get('produto__id')), x['data_e_quantidade']))

        # Lista para armazenar o estado atual de cada produto
        current_state = {}

        # Lista para armazenar os dados finais para o gráfico
        datasets = []

        for item in combined_queryset:
            produto_id = item.get('id', item.get('produto__id'))

            # Inicializa o estado do produto se ainda não estiver na lista
            if produto_id not in current_state:
                current_state[produto_id] = {
                    'label': item.get('produto__nome', item.get('nome')),
                    'data': [],
                    'quantidade_acumulada': item['quantidade_total'],
                }

            # Calcula a quantidade acumulada com base no tipo de movimentação (entrada ou saída)
            tipo_movimentacao = item.get('tipo', None)
            if tipo_movimentacao == 'entrada':
                current_state[produto_id]['quantidade_acumulada'] += item['quantidade_total']
            elif tipo_movimentacao == 'saida':
                current_state[produto_id]['quantidade_acumulada'] -= item['quantidade_total']

            # Adiciona os dados ao estado atual do produto
            current_state[produto_id]['data'].append({
                'x': item['data_e_quantidade'].timestamp() * 1000,  # Converte para milissegundos
                'y': current_state[produto_id]['quantidade_acumulada'],
                'r': current_state[produto_id]['quantidade_acumulada'],
            })

        # Converte o estado atual dos produtos em uma lista para o gráfico bubble
        datasets = [{'label': data['label'], 'data': data['data']} for data in current_state.values()]

        data = {'datasets': datasets}
        return JsonResponse(data)
