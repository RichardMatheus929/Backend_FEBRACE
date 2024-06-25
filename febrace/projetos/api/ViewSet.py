from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework import status
from projetos.models import Projeto
from .Serializers import ProjetoSerializer

import random

class ProjetoViewSet(ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    # filter_backends = [filters.SearchFilter]
    filterset_fields = ['id', 'ano']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        allprojetos = serializer.data

        random.shuffle(allprojetos)

        return Response(allprojetos)

    # def list(self, request, *args, **kwargs):
    #     # Obtém os parâmetros da query string
    #     query_params = request.query_params

    #     projetos = self.get_queryset()
    #     serializer = self.get_serializer(projetos,many=True)

    #     # JSON padrão a ser retornado
    #     response_data = {
    #         "message": "Este é um JSON padrão para todas as requisições GET",
    #         "status": "success",
    #         "data": serializer.data, #todos os dados do meu serializer ProjetoSerializer
    #         "query_params": query_params.dict()  # Converte os parâmetros da query string em um dicionário
    #     }

    #     return Response(response_data, status=status.HTTP_200_OK)
