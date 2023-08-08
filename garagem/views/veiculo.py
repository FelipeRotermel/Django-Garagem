from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor
from garagem.serializers import CategoriaSerializer, MarcaSerializer, VeiculoSerializer, AcessorioSerializer, CorSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VeiculoDetailSerializer
        return VeiculoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer