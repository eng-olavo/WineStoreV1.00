from django.contrib import admin
from .models import Vinho


@admin.register(Vinho)
class VinhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'safra')


