from django.db import models


class Produtos(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    nome = models.CharField(
        max_length=65, null=False, blank=False
    )
    marca = models.CharField(
        max_length=65, null=False, blank=False
    )
    descricao = models.TextField(
        max_length=255
    )

    preco = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False
    )
    quantidade = models.IntegerField(
        default=0, null=False, blank=False
    )
    imagem = models.ImageField(
        # A pasta onde as imagens serão armazenadas
        upload_to='gerencia/static/gerencia/images',
        null=True,  # Pode ser nulo, se desejar
        blank=True,  # Pode ser em branco, se desejar
    )
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True) 


class LogEstoque(models.Model):
    id = models.AutoField(
        primary_key=True
    ) 
    produto = models.ForeignKey(
        Produtos, on_delete=models.CASCADE
    )
    quantidade = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    tipo = models.CharField(
        max_length=10, 
        choices=[
            ('entrada', 'Entrada'), 
            ('saida', 'Saída')
        ]
    )
    data_movimentacao = models.DateTimeField(
        auto_now_add=True
    )


class SaldoEstoque(models.Model):
    log = models.ForeignKey(
        Produtos, on_delete=models.CASCADE
    )
    quantidadet = models.IntegerField(
        default=0
    )
    data_mov = models.DateTimeField(
        auto_now_add=True
    )


class Fornecedores(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    nome = models.CharField(
        max_length=64, null=False, blank=False
    )
    endereco = models.CharField(
        max_length=255, null=False, blank=False
    )


class Transacoes(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    produto_id = models.ForeignKey('Produtos', on_delete=models.CASCADE)
    tipo = models.TextField()
    quantidade = models.IntegerField(
        default=0, null=False, blank=False
    )
    data = models.DateTimeField(auto_now_add=True)


class DadosTreinamento(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    produto_id = models.ForeignKey('Produtos', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField(
        default=0, null=False, blank=False
    )
    preco = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False
    )


class DadosPrevisao(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    produto_id = models.ForeignKey('Produtos', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField(
        default=0, null=False, blank=False
    )
    preco = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False
    )


objetos = models.Manager()