from rest_framework import viewsets, generics
from .models import Alunos, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer,ListaMatriculaSerealizer, ListaAlunosMatriculadosSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    # Exibindo todos os lunos
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    # Exibir todos os cursos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    # Exibir Matrículas
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaSerealizer
    
class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
