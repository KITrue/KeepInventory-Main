# Generated by Django 4.2.3 on 2023-09-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0002_remove_produtos_fornecedor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.TextField(max_length=255),
        ),
    ]
