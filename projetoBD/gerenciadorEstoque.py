from psycopg2 import sql
from livro import Livro

class GerenciadorEstoque:
    def __init__(self, conexao):
        self.conexao = conexao

    def adicionar_livro(self, livro):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO minha_tabela (titulo, autor, quantidade, preco, sinopse) VALUES (%s, %s, %s, %s, %s)",
                       (livro.titulo, livro.autor, livro.quantidade, livro.preco, livro.sinopse))
        self.conexao.commit()
        cursor.close()

    def buscar_livro(self, titulo):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM minha_tabela WHERE titulo = %s", (titulo,))
        livro = cursor.fetchone()
        cursor.close()
        if livro:
            return Livro(livro[1], livro[2], livro[3], livro[4], livro[5])
        else:
            return None

    def listar_livros(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM minha_tabela")
        livros = []
        for row in cursor.fetchall():
            livros.append(Livro(row[1], row[2], row[3], row[4], row[5]))
        cursor.close()
        return livros
    
    def excluir_livro(self, titulo):
        cursor = self.conexao.cursor()
        sql = "DELETE FROM minha_tabela WHERE titulo = %s"
        values = (titulo,)
        cursor.execute(sql, values)
        self.conexao.commit()
        cursor.close()
