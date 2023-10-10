from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('listarlivros', views.listar_livros, name='listar_livros'),
    path('criar/', views.criar_livro, name='criar_livro'),
    path('editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('deletar/<int:pk>/', views.deletar_livro, name='excluir_livro'),
    path('relatorio_estoque', views.gerar_relatorio, name='gerar_relatorio_estoque')
]