from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm
from .GerenciadorLivros import GerenciadorLivros

# Create your views here.

def pagina_inicial(request):
    return render(request, 'estoque/pagina_inicial.html')

def listar_livros(request):
    livros = GerenciadorLivros.listar_livros()
    return render(request, 'estoque/listar_livros.html', {'livros': livros})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            GerenciadorLivros.criar_livro(
                titulo=form.cleaned_data['titulo'],
                autor=form.cleaned_data['autor'],
                quantidade_em_estoque=form.cleaned_data['quantidade_em_estoque']
            )
            return redirect(listar_livros)
    else:
        form = LivroForm()
    return render(request, 'estoque/criar_livro.html', {'form': form})

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            GerenciadorLivros.atualizar_livro(
                pk=pk,
                titulo=form.cleaned_data['titulo'],
                autor=form.cleaned_data['autor'],
                quantidade_em_estoque=form.cleaned_data['quantidade_em_estoque'])
            
            return redirect(listar_livros)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'estoque/editar_livro.html', {'form': form, 'livro': livro})

def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect(listar_livros)
    return render(request, 'estoque/deletar_livro.html', {'livro': livro})

def gerar_relatorio(request):
    return GerenciadorLivros.gerar_relatorio()