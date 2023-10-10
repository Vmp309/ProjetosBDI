from .models import Livro
from .GerenciadorRelatorio import GerenciadorRelatorio

class GerenciadorLivros:
    @classmethod
    def listar_livros(cls):
        return Livro.objects.all()

    @classmethod
    def criar_livro(cls, titulo, autor, quantidade_em_estoque):
        livro = Livro(titulo=titulo, autor=autor, quantidade_em_estoque=quantidade_em_estoque)
        livro.save()
        return livro

    @classmethod
    def obter_livro(cls, pk):
        return Livro.objects.get(pk=pk)

    @classmethod
    def atualizar_livro(cls, pk, titulo, autor, quantidade_em_estoque):
        livro = Livro.objects.get(pk=pk)
        livro.titulo = titulo
        livro.autor = autor
        livro.quantidade_em_estoque = quantidade_em_estoque
        livro.save()
        return livro

    @classmethod
    def deletar_livro(cls, pk):
        livro = Livro.objects.get(pk=pk)
        livro.delete()
    
    @classmethod
    def gerar_relatorio(cls):
        livros = Livro.objects.all()
        
        response = GerenciadorRelatorio.gerar_relatorio_estoque(livros)

        return response