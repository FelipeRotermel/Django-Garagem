from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor

class CorSerializer(ModelSerializer):
        class Meta:
            model = Cor
            fields = "__all__"