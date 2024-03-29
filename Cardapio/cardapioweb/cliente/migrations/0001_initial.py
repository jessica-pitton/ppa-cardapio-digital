# Generated by Django 4.2.1 on 2023-06-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=200)),
                ('criacao', models.DateTimeField(verbose_name='data de criacão')),
                ('alteracao', models.DateTimeField(verbose_name='data de alteração')),
            ],
        ),
    ]
