from django.db import models


class Vinho(models.Model):
    nome = models.CharField(max_length=128)
    safra = models.IntegerField()

    def __str__(self):
        return self.nome

