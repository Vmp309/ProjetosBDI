from psycopg2 import sql
from Seller import Vendedor
from Client import Cliente
from Livro import Livro

class GerenciadorBD:
    def __init__(self, conexao):
        self.conexao = conexao

# Funções Livro

    def adicionar_livro(self, livro):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO livro (id_livro, titulo, autor, origem, categoria, sinopse, quantidade, valor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (livro.id_livro, livro.titulo, livro.autor, livro.origem, livro.categoria, livro.sinopse, livro.quantidade, livro.valor))
        self.conexao.commit()
        cursor.close()

    def verificar_id_Livro(self, id_livro):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE id_livro = %s", (id_livro, ))
        verificador_id = cursor.fetchone()
        cursor.close()
        if verificador_id == None:
            return False
        else:
            return True

    def verificar_titulo_Livro(self, titulo):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE titulo = %s", (titulo, ))
        verificador_titulo = cursor.fetchone()
        cursor.close()
        if verificador_titulo == None:
            return False
        else:
            return True

    def buscar_titulo_Livro(self, titulo):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE titulo = %s", (titulo,))
        livro = cursor.fetchone()
        cursor.close()
        if livro:
            return Livro(livro[0], livro[1], livro[2], livro[3], livro[4], livro[5], livro[6], livro[7])
        else:
            return None

    def buscar_faixa_preco_Livro(self, maior, menor):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE valor BETWEEN %s AND %s", (menor, maior))
        livros = []
        for row in cursor.fetchall():
            livros.append(Livro(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        cursor.close()
        return livros
        


    def buscar_categoria_Livro(self, categoria):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE categoria = %s", (categoria, ))
        livros = []
        for livro in cursor.fetchall():
            livros.append(Livro(livro[0], livro[1], livro[2], livro[3], livro[4], livro[5], livro[6], livro[7]))
        return livros

    def buscar_local_Livro(self, origem):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE origem = %s", (origem, ))
        livros = []
        for livro in cursor.fetchall():
            livros.append(Livro(livro[0], livro[1], livro[2], livro[3], livro[4], livro[5], livro[6], livro[7]))
        return livros


    def buscar_tituloFiltrado_Livro(self, titulo):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE titulo = %s AND quantidade < 5", (titulo,))
        livro = cursor.fetchall()
        cursor.close()
        if livro:
            return Livro(livro[0], livro[1], livro[2], livro[3], livro[4], livro[5], livro[6], livro[7])
        else:
            return None


    def buscar_faixa_precoFiltrado_Livro(self, maior, menor):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE quantidade < 5 AND valor BETWEEN %s AND %s", (menor, maior))
        livros = []
        for row in cursor.fetchall():
            livros.append(Livro(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        cursor.close()
        return livros

    def buscar_categoriaFiltrado_Livro(self, categoria):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE categoria = %s AND quantidade < 5", (categoria, ))
        livros = []
        for livro in cursor.fetchall():
            livros.append(Livro(livro[0], livro[1], livro[2], livro[3], livro[4], livro[5], livro[6], livro[7]))
        return livros

    def buscar_localFiltrado_Livro(self, origem):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livro WHERE origem = %s AND quantidade < 5", (origem, ))
        livros = []
        for livro in cursor.fetchall():
            livros.append(Livro(livro[0], livro[1], livro[2], livro[3], livro[4], livro[5], livro[6], livro[7]))
        return livros
# Funções Vendedor

    # Adiciona Vendedor
    def adicionar_vendedor(self, vendedor):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO vendedor (cpf, username, password, nome) VALUES (%s, %s, %s, %s)",
        (vendedor.cpf, vendedor.username, vendedor.password, vendedor.nome))
        self.conexao.commit()
        cursor.close()

    # Retorna Falso se o cpf do cliente passado já estiver no BD
    def verificar_cpf_Vendedor(self, cpf):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM vendedor WHERE cpf = %s", (cpf, ))
        verificador_cpf = cursor.fetchone()
        cursor.close()
        if verificador_cpf == None:
            return False
        else:
            return True

    def verificar_user_Vendedor(self, username):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM vendedor WHERE username = %s", (username, ))
        verificador_user = cursor.fetchone()
        cursor.close()
        if verificador_user == None:
            return False
        else:
            return True



    def verificar_senha_Vendedor(self, login, senha):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM vendedor WHERE username = %s", (login, ))
        linha = cursor.fetchone() # linha recebe uma tupla com todas as infos do usuario
        cursor.close()
        password = linha[2] # Pega o campo de senha da tupla linha
        if password == senha:
            return True
        else:
            return False

    def vendedor_para_login(self, login, senha):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM vendedor WHERE username = %s", (login, ))
        linha_vendedor = cursor.fetchone()
        cursor.close()
        vendedor = Vendedor(cpf=linha_vendedor[0], username=linha_vendedor[1], password=linha_vendedor[2], nome=linha_vendedor[3])
        return vendedor


# Funções CLiente
    def adicionar_cliente(self, cliente):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO cliente (cpf, username, password, nome, isFlamengo, isOnePieceFan, isSousa, endereco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (cliente.cpf, cliente.username, cliente.password, cliente.nome, cliente.isFlamengo, cliente.isOnePieceFan, cliente.isSousa, cliente.endereco))
        self.conexao.commit()
        cursor.close()


    def verificar_cpf_Cliente(self, cpf):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM cliente WHERE cpf = %s", (cpf, ))
        verificador_cpf = cursor.fetchone()
        cursor.close()
        if verificador_cpf == None:
            return False
        else:
            return True

    def verificar_user_Cliente(self, username):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM cliente WHERE username = %s", (username, ))
        verificador_user = cursor.fetchone()
        cursor.close()
        if verificador_user == None:
            return False
        else:
            return True


    def verificar_senha_Cliente(self, login, senha):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM cliente WHERE username = %s", (login, ))
        linha = cursor.fetchone() # linha recebe uma tupla com todas as infos do usuario
        cursor.close()
        password = linha[2] # Pega o campo de senha da tupla linha
        if password == senha:
            return True
        else:
            return False


    def client_para_login(self, login, senha):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM cliente WHERE username = %s", (login, ))
        linha_cliente = cursor.fetchone()
        cursor.close()
        cliente = Cliente(cpf=linha_cliente[0], username=linha_cliente[1], password=linha_cliente[2], nome=linha_cliente[3],isFlamengo=linha_cliente[4], isOnePieceFan=linha_cliente[5], isSousa=linha_cliente[6], endereco=linha_cliente[7])
        return cliente




# Utilidades

    def apagar_tudo(self, nome_tabela):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM %s", nome_tabela)
        self.conexao.commit()
        cursor.close()