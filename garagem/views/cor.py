from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor
from garagem.serializers import CategoriaSerializer, MarcaSerializer, VeiculoSerializer, AcessorioSerializer, CorSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
