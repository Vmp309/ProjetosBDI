from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm, ClienteCreationForm, VendedorCreationForm, LoginForm
from .GerenciadorLivros import GerenciadorLivros
from .GerenciadorCliente import GerenciadorCliente
from .GerenciadorVendedor import GerenciadorVendedor
from .auth import authenticate
from django.http import HttpResponseRedirect
from .Vendas import Vendas

# Create your views here.

"""class CustomLoginView(auth_views.LoginView):

    def form_valid(self, form):
        # Lógica personalizada aqui, se necessário
        return HttpResponseRedirect(self.get_success_url('estoque'))"""


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
                valor=form.cleaned_data['valor'],
                origem=form.cleaned_data['origem'],
                categoria=form.cleaned_data['categoria']
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
                valor=form.cleaned_data['valor'],
                origem=form.cleaned_data['origem'],
                categoria=form.cleaned_data['categoria'])
            
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
    return Vendas.gerar_relatorio()

def register_cliente(request):
    if request.method == 'POST':
        form = ClienteCreationForm(request.POST)
        if form.is_valid():
            GerenciadorCliente.cadastrar(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                nome=form.cleaned_data['nome'],
                cpf=form.cleaned_data['cpf'],
                isflamengo=form.cleaned_data['isflamengo'],
                onePiece=form.cleaned_data['onePiece'],
                endereco=form.cleaned_data['endereco']
            )
            form.save()
            return redirect('login')
    else:
        form = ClienteCreationForm()
    return render(request, 'usuarios/register_cliente.html', {'form': form})

def register_vendedor(request):
    if request.method == 'POST':
        form = VendedorCreationForm(request.POST)
        if form.is_valid():
            GerenciadorVendedor.cadastrar_Vendedor(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                nome=form.cleaned_data['nome'],
                cpf=form.cleaned_data['cpf']
            )
            form.save()
            return redirect('login')
    else:
        form = ClienteCreationForm()
    return render(request, 'usuarios/register_vendedor.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        auth = authenticate(form.username, form.password)
        if auth[0] == True:
            return render(request, 'usuarios/profile.html')

