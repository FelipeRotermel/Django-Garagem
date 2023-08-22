from django.db import models
from .cor import Cor
from .modelo import Modelo
from uploader.models import Image
from .acessorio import Acessorio

class Veiculo(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField()
    placa = models.CharField(max_length=10, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    descricao = models.CharField(max_length=250,blank=True, null=True)
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="veiculos")
    
    capas = models.ManyToManyField(Image, related_name="Veiculos")

    def __str__(self):
        return f"{self.modelo} {self.ano} {self.cor}) "