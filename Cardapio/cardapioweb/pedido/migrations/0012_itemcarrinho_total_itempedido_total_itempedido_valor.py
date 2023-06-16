# Generated by Django 4.2.2 on 2023-06-16 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pedido", "0011_remove_itempedido_produto_itempedido_produto"),
    ]

    operations = [
        migrations.AddField(
            model_name="itemcarrinho",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="itempedido",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="itempedido",
            name="valor",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
