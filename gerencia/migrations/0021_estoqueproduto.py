# Generated by Django 4.2.3 on 2023-12-01 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("gerencia", "0020_alter_logestoque_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="EstoqueProduto",
            fields=[
                (
                    "produto",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="gerencia.produtos",
                    ),
                ),
                ("quantidade_total", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
