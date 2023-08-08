from django.db import models
from .marca import Marca
from .categoria import Categoria
from .cor import Cor
from uploader.models import Image

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    descricao = models.CharField(max_length=250,blank=True, null=True)

    capa = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="+", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} {self.cor}) "
