# Generated by Django 4.2.3 on 2023-11-20 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("gerencia", "0011_alter_produtos_data_saida"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogEstoque",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[("entrada", "Entrada"), ("saida", "Saída")],
                        max_length=10,
                    ),
                ),
                ("quantidade", models.PositiveIntegerField(blank=True, null=True)),
                ("data_movimentacao", models.DateTimeField(auto_now_add=True)),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerencia.produtos",
                    ),
                ),
            ],
        ),
    ]
