from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nascionalidade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nome.upper()} ({self.id}) "
    
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id}) "

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id}) "
    
class Cor(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.descricao} ({self.id}) "
    
    class Meta:
        verbose_name_plural = "cores"
        verbose_name= "cor"

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} {self.cor}) "
