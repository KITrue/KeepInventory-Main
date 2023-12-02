from django.http import JsonResponse
from django.views import View
from django.db.models import F, Sum
from .models import SaldoEstoque

class ChartDataView(View):
    def get(self, request, *args, **kwargs):
        # Realiza a junção de SaldoEstoque usando annotate para calcular a soma da quantidade
        saldo_queryset = SaldoEstoque.objects.annotate(
            data_e_quantidade=F('data_mov'),
            quantidade_total=F('quantidadet')
        ).values('log__id', 'log__nome', 'data_e_quantidade', 'quantidade_total')

        # Agrupa os resultados pelo log__id
        grouped_data = {}
        for item in saldo_queryset:
            log_id = item.get('log__id')
            if log_id not in grouped_data:
                grouped_data[log_id] = {
                    'label': item['log__nome'],
                    'data': [],
                }
            grouped_data[log_id]['data'].append({
                'x': item['data_e_quantidade'].timestamp() * 1000,  # Converte para milissegundos
                'y': item['quantidade_total'],
                'r': 30,
            })

        # Converte o dicionário agrupado em uma lista para o gráfico bubble
        datasets = [{'label': data['label'], 'data': data['data']} for data in grouped_data.values()]

        data = {'datasets': datasets}
        return JsonResponse(data)
