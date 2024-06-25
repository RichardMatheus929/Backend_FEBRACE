from rest_framework.serializers import ModelSerializer
from projetos.models import Projeto

class ProjetoSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = (
                'id',
                'nome',
                'categoria_premiacao',
                'cidade',
                'escola',
                'estado',
                'ano'
                  )