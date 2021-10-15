from django.contrib import admin
from .models import Vinho


@admin.register(Vinho)
class VinhoAdmin(admin.ModelAdmin):
    list_display = ('nome','uvas','tipo','acucar',
                    'safra','nacionalidade', 'vinicola',
                    'reserva', 'alcool', 'temperatura', 'volume',
                    'amadurecimento', 'guarda', 'visual', 'olfativo',
                    'gustativo',)


