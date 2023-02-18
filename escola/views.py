from rest_framework import viewsets
from .models import Alunos, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    # Exibindo todos os lunos
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    # Exibir todos os cursos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    # Exibir todos os cursos
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

