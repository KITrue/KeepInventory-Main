# Generated by Django 4.2.3 on 2023-09-18 02:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gerencia", "0007_merge_20230917_2105"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produtos",
            name="imagem",
            field=models.ImageField(
                blank=True, null=True, upload_to="static/gerencia/images"
            ),
        ),
    ]