from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nascionalidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome.upper()} ({self.id}) "
    
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id}) "
