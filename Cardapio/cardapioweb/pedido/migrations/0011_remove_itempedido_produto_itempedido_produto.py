# Generated by Django 4.2.2 on 2023-06-16 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0004_imagemproduto_produto"),
        ("pedido", "0010_remove_itemcarrinho_observacao"),
    ]

    operations = [
        migrations.RemoveField(model_name="itempedido", name="produto",),
        migrations.AddField(
            model_name="itempedido",
            name="produto",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="produto.produto",
            ),
        ),
    ]
