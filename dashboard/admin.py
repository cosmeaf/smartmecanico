from django.contrib import admin
from .models import Carro, Servicos, Agendamento, Combustivel, Endereco, Cliente, DiasVisita, HorarioAgendamento


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'ano', 'kilometragem', 'cliente',)


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(DiasVisita)
class DiasVisitaAdmin(admin.ModelAdmin):
    list_display = ('dia',)


@admin.register(HorarioAgendamento)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('horario',)


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'servico', 'placa', 'dias_visita', 'horarios', 'status', 'data_criacao',)


@admin.register(Combustivel)
class CombustivelAdmin(admin.ModelAdmin):
    list_display = ('litros', 'preco', 'placa', 'kilometragem', 'data_compra',)


# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
#     list_display = ('placa', 'endereco')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf',)