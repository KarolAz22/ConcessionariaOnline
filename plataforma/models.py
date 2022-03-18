from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Veiculo(models.Model):
    choices_combustivel = (('G','Gasolina'),
                                            ('A','Alcool'),
                                            ('D','Diesel'),
                                            ('E', 'Eletrico'), 
                                            ('F','Flex'))

    imagem1 = models.FileField(upload_to='img')
    imagem2 = models.ImageField(upload_to='img')
    imagem3 = models.ImageField(upload_to='img')
    valor = models.FloatField()
    modelo = models.CharField(max_length=30)
    kmRodados = models.IntegerField()
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    tipo_combustivel = models.CharField(choices=choices_combustivel, max_length=1)
    descricao = models.TextField(max_length=255)
    telefone = models.BigIntegerField()
    cidade = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    rua = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.modelo

class Contato(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField(max_length=255)