# Generated by Django 4.2.3 on 2023-09-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0005_produtos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(
                blank=True, null=True, upload_to='gerencia/static/gerencia/images'),
        ),
    ]
