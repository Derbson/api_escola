from rest_framework import serializers
from .models import Alunos, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = ["id", "nome", "rg", "cpf", "data_nascimento"]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"