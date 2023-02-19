from django.urls import path, include
from .views import AlunosViewSet, CursosViewSet, MatriculaViewSet,ListaMatriculaAluno,ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Matriculas')


urlpatterns = [
     path('', include(router.urls)),
     path('aluno/<int:pk>/matriculas/', ListaMatriculaAluno.as_view()),
     path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]



