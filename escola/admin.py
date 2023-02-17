from django.contrib import admin
from .models import Alunos, Curso


class ListarAlunos(admin.ModelAdmin):
    list_display = ("id", "nome","cpf", "data_nascimento",)
    list_display_links = ("id", "nome",)
    search_fields = ("nome",)
    list_per_page = 20
    

class ListarCurso(admin.ModelAdmin):
    list_display = ("id","descricao" ,"codigo_curso", )
    list_display_links = ("id", "descricao",)
    search_fields = ("descricao",)

admin.site.register(Alunos,ListarAlunos)
admin.site.register(Curso,ListarCurso)


