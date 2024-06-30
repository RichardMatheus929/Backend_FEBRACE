from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projetos.models import Projeto
from .Serializers import ProjetoSerializer

import random

def remove_duplicate_project(allprojetos):
    unique_projects = []
    unique_names = set()
    for project in allprojetos:
        if project['nome'] in unique_names:
            pass
        else:
            unique_names.add(project['nome'])
            unique_projects.append(project)

    return unique_projects

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
        allprojetos = remove_duplicate_project(allprojetos)

        random.shuffle(allprojetos)

        return Response(allprojetos)

