from django.urls import path # Modulo do Django para criar URLS
from .views import * # Importe todas as suas classes do views.py, o * importa todas as classes do View, ou importar por nome

urlpatterns = [
    # path(
    # 'caminho/da/url'),
    # ClasseLáDoView.as_view(),
    # name="nomeDessaUrl"
    path('inicio/', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
]
