# Generated by Django 4.2.3 on 2023-09-12 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0003_alter_produtos_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='marca',
            field=models.CharField(default=0, max_length=65),
            preserve_default=False,
        ),
    ]