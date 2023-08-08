from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"