# Generated by Django 4.2.2 on 2023-06-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pedido", "0005_alter_itempedido_pedido"),
    ]

    operations = [
        migrations.AddField(
            model_name="itemcarrinho",
            name="valor",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
