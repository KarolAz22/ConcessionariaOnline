from django.contrib import admin
from plataforma.models import  Veiculo, Contato

# Register your models here.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'cidade', 'valor', 'telefone',)
    list_editable = ('valor', 'telefone')
    list_filter = ('cidade', 'modelo')

admin.site.register(Contato)

