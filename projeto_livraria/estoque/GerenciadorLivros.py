from .models import Livro
from .GerenciadorRelatorio import GerenciadorRelatorio

class GerenciadorLivros:
    @classmethod
    def listar_livros(cls):
        return Livro.objects.all()

    @classmethod
    def criar_livro(cls, titulo, autor, quantidade_em_estoque, valor,origem, categoria):
        livro = Livro(titulo=titulo, autor=autor, quantidade_em_estoque=quantidade_em_estoque, valor=valor,origem=origem, categoria=categoria)
        livro.save()
        return livro

    @classmethod
    def obter_livro(cls, pk):
        return Livro.objects.get(pk=pk)

    @classmethod
    def atualizar_livro(cls, pk, titulo, autor, quantidade_em_estoque, valor,origem, categoria):
        livro = Livro.objects.get(pk=pk)
        livro.titulo = titulo
        livro.autor = autor
        livro.quantidade_em_estoque = quantidade_em_estoque
        livro.valor = valor
        livro.origem=origem
        livro.categoria=categoria
        livro.save()
        return livro

    @classmethod
    def deletar_livro(cls, pk):
        livro = Livro.objects.get(pk=pk)
        livro.delete()
    
    @classmethod
    def gerar_relatorio(cls, dataInicio, dataFim):
        with connection.cursor() as cursor:
            relatorio = cursor.callproc(gerar_relatorio_livros, dataInicio, dataFim)
            return relatorio
        
        # livros = Livro.objects.all()
        # response = GerenciadorRelatorio.gerar_relatorio_estoque(livros)
        # return response