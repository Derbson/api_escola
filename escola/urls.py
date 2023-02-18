from django.urls import path, include
from .views import AlunosViewSet, CursosViewSet, MatriculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Cursos')


urlpatterns = [
     path('', include(router.urls))
]



