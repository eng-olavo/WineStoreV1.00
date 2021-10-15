from django.db import models


class Vinho(models.Model):
    nome = models.CharField(max_length=128, name='nome')
    uvas = models.CharField(max_length=128, name='uvas')
    tipo = models.CharField(max_length=32, name='tipo')
    acucar = models.CharField(max_length=32, name='acucar')
    safra = models.IntegerField(name='safra')
    nacionalidade = models.CharField(max_length=32, name='nacionalidade')
    vinicola = models.CharField(max_length=32, name='vinicola')
    reserva = models.CharField(max_length=32, name='reserva')
    alcool = models.IntegerField(name='alcool')
    temperatura = models.IntegerField(name='temperatura')
    volume = models.IntegerField(name='volume')
    amadurecimento = models.CharField(max_length=128, name='amadurecimento')
    guarda = models.IntegerField(name='guarda')
    visual = models.CharField(max_length=32, name='visual')
    olfativo = models.TextField(max_length=256, name='olfativo')
    gustativo = models.TextField(max_length=256, name='gustativo')


    def __str__(self):
        return self.nome

