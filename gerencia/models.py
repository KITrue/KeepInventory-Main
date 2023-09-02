from django.db import models


class Produtos(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    nome = models.CharField(
        max_length=65, null=False, blank=False
    )
    descricao = models.TextField()
    preco = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False
    )
    quantidade = models.IntegerField(
        default=0, null=False, blank=False
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
