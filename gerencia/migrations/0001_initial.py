# Generated by Django 4.2.3 on 2023-09-02 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fornecedores",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=64)),
                ("endereco", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Produtos",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=65)),
                ("descricao", models.TextField()),
                ("preco", models.DecimalField(decimal_places=2, max_digits=8)),
                ("quantidade", models.IntegerField(default=0)),
                (
                    "fornecedor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerencia.fornecedores",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transacoes",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("tipo", models.TextField()),
                ("quantidade", models.IntegerField(default=0)),
                ("data", models.DateTimeField(auto_now_add=True)),
                (
                    "produto_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerencia.produtos",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DadosTreinamento",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("data", models.DateTimeField(auto_now_add=True)),
                ("quantidade", models.IntegerField(default=0)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "produto_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerencia.produtos",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DadosPrevisao",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("data", models.DateTimeField(auto_now_add=True)),
                ("quantidade", models.IntegerField(default=0)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "produto_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerencia.produtos",
                    ),
                ),
            ],
        ),
    ]
