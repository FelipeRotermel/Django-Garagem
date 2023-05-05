from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"

class VeiculoListSerializer(ModelSerializer):    
    class Meta:
        model = Veiculo
        fields = ["id", "modelo", "marca", "categoria"]

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1 