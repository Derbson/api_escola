from django.urls import path, include
from .views import alunos


urlpatterns = [
    path('alunos', alunos)
]


