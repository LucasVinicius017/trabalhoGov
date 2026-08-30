from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("usuarios/", views.usuarios, name="usuarios"),
    path("usuarios/novo/", views.novo_usuario, name="novo_usuario"),
    path("usuarios/editar/<int:id>/", views.editar_usuario, name="editar_usuario"),
    path("usuarios/excluir/<int:id>/", views.excluir_usuario, name="excluir_usuario"),

    path("pontos/", views.pontos, name="pontos"),
    path("pontos/novo/", views.novo_ponto, name="novo_ponto"),
    path("pontos/editar/<int:id>/", views.editar_ponto, name="editar_ponto"),
    path("pontos/excluir/<int:id>/", views.excluir_ponto, name="excluir_ponto"),

    path("relatorios/", views.relatorios, name="relatorios"),    
    path("manutencoes/", views.manutencoes, name="manutencoes"),
    path("manutencoes/nova/", views.nova_manutencao, name="nova_manutencao"),
    path("manutencoes/editar/<int:id>/", views.editar_manutencao, name="editar_manutencao"),
    path("manutencoes/excluir/<int:id>/", views.excluir_manutencao, name="excluir_manutencao"),
    path("logout/", views.logout, name="logout"),
]