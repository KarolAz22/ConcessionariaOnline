# Generated by Django 4.0.3 on 2022-03-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0006_alter_veiculo_kmrodados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='cidade',
            field=models.CharField(max_length=60),
        ),
    ]
