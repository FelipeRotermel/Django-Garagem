from django.db import models
from .marca import Marca
from .categoria import Categoria

class Modelo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nome.upper()} ({self.id}) "