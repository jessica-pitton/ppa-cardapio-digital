# Generated by Django 4.2.2 on 2023-06-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_cliente_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=200, null=True),
        ),
    ]