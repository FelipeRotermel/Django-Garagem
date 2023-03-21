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
        verbose_name_plural = "Cores"

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.modelo} ({self.id}) "
