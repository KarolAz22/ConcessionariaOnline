# Generated by Django 4.0.3 on 2022-03-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0011_veiculo_imagem2_veiculo_imagem3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
    ]
