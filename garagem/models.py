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

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"{self.modelo} ({self.id}) "
