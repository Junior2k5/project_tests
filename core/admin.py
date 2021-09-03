from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Recurso, Cliente, Preco

# Register your models here.
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'icone', 'ativo', 'modificado')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'ativo', 'modificado')

@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = ('plano', 'capacidade', 'ativo', 'modificado')