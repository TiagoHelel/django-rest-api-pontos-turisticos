from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField

class PontoTuristicoSerializer(ModelSerializer):
    # atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = [
            'id', 'nome', 'descricao', 'aprovado', 'endereco', 'foto',
            'endereco', 
            'descricao_completa', 'descricao_completa2'
            ]
        # fields = [
        #     'id', 'nome', 'descricao', 'aprovado', 'endereco', 'foto',
        #     'atracoes', 'comentarios', 'avaliacoes', 'endereco', 
        #     'descricao_completa', 'descricao_completa2'
        #     ]

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'