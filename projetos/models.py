from typing import Any
from django.db import models

# Create your models here.


class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=260)
    categoria_premiacao = models.CharField(max_length=90)
    escola = models.CharField(max_length=110)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    ano = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nome[:45] + "... " + " -> "+str(self.id)
