# Generated by Django 4.2.1 on 2023-06-16 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_imagemproduto_produto'),
        ('pedido', '0007_remove_itemcarrinho_produto_itemcarrinho_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.produto'),
        ),
    ]
