from django.contrib import admin
from .models import Ciclo, Dica, Sintoma

@admin.register(Ciclo)
class CicloAdmin(admin.ModelAdmin):
    list_display = ('data_inicio', 'data_proxima', 'data_fim', 'usuario')
    search_fields = ('usuario__username',)
    list_filter = ('data_inicio', 'data_fim')

@admin.register(Dica)
class DicaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)
    list_filter = ('titulo',)

@admin.register(Sintoma)
class SintomaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data', 'usuario')
    search_fields = ('descricao', 'usuario__username')
    list_filter = ('data',)
