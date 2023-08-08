from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"