from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Livro
from .forms import LivroForm
from .GerenciadorLivros import GerenciadorLivros
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

# Create your views here.

class CustomLoginView(auth_views.LoginView):

    def form_valid(self, form):
        # Lógica personalizada aqui, se necessário
        return HttpResponseRedirect(self.get_success_url('estoque'))


def pagina_inicial(request):
    return render(request, 'html/index.html')

def listar_livros(request):
    livros = GerenciadorLivros.listar_livros()
    return render(request, 'html/listar_livros.html', {'livros': livros})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            GerenciadorLivros.criar_livro(
                titulo=form.cleaned_data['titulo'],
                autor=form.cleaned_data['autor'],
                quantidade_em_estoque=form.cleaned_data['quantidade_em_estoque'],
                valor=form.cleaned_data['valor']
            )
            return redirect(listar_livros)
    else:
        form = LivroForm()
    return render(request, 'html/criar_livro.html', {'form': form})

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            GerenciadorLivros.atualizar_livro(
                pk=pk,
                titulo=form.cleaned_data['titulo'],
                autor=form.cleaned_data['autor'],
                quantidade_em_estoque=form.cleaned_data['quantidade_em_estoque'],
                valor=form.cleaned_data['valor'])
            
            return redirect(listar_livros)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'html/editar_livro.html', {'form': form, 'livro': livro})

def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect(listar_livros)
    return render(request, 'html/deletar_livro.html', {'livro': livro})

def gerar_relatorio(request):
    return GerenciadorLivros.gerar_relatorio()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})
