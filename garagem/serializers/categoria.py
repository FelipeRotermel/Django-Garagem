from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"