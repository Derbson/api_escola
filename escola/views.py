from rest_framework import viewsets
from .models import Alunos, Curso
from .serializer import AlunoSerializer, CursoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    # Exibindo todos os lunos
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    # Exibir todos os cursos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

