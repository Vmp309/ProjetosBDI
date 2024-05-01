from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from .views import CustomLoginView

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('listarlivros', views.listar_livros, name='listar_livros'),
    path('criar/', views.criar_livro, name='criar_livro'),
    path('editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('deletar/<int:pk>/', views.deletar_livro, name='excluir_livro'),
    path('relatorio_estoque', views.gerar_relatorio, name='gerar_relatorio_estoque'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]