# Generated by Django 4.2.1 on 2023-06-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_alteracao_alter_cliente_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=15),
        ),
    ]
