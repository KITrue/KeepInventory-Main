from django.db import models

class produto(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
    