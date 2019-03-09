from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
# Cria uma classe com herança de TemplateView para exibir um arquivo HTML normal (com o conteúdo dele)
# Esta página/método/classe
class PaginaInicialView(TemplateView): # Nome do arquivo que vai ser utilizado para renderizar a página
    template_name = "index.html"

class SobreView(TemplateView):
    template_name = "sobre.html"
