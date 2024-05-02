from django import django
from .models import Livros

class MenuBuscar:
    tipo = None # Tipo = 0 cliente, Tipo = 1 vendedor, tipo = 3 compras
    
    def exibir_menu(self, tipo ):
            self.tipo = tipo        
            print("Consulta de livros")
            print("1) Pesquisar por Nome.")
            print("2) Pesquisar por Faixa de Preço")
            print("3) Pesquisar por Categoria")
            print("4) Foi fabricado em Mari")
            opcao = input("Digite a opcao:")
            if (opcao == 1): # Pesquisa o livro pelo nome
                nome = input("Digite o nome do livro: ")
                livro = consultarNome(nome)
                if (livro != None):# Se o livro não for None, retorna o id do livro
                    return livro
                else:
                    return
            elif (opcao == 2): # Pesquisa por uma faixa de preço
                maior = input("Digite o maior preço\n->")
                menor = input("Digite o menor preço\n->")
                livro = consultarPreco(maior, menor)
                if (livro != None): # Se o livro não for None, retorna o id do livro
                    return livro
                else:
                    return
            elif (opcao == 3): # Prsquisa por Categoria
                categoria = input("Digite a Categoria\n>") 
                livros = consultarCategoria(categoria)
                if (livros != None): # Se a lista de livros não for None, retorna a lista
                    return livros
                else: 
                    return 
            elif (opcao == 4): # Consulta os livros feitos em Mari
                livros = consultarMari()
                if (livros != None): # Se a lista de livros não for None, retorna a lista
                    return livros
                else:
                    return
            else:
                return
    
    
    def consultarNome(self , nome):
        livro = Livro.object.get(nome==nome)
        if (tipo == "operação_vendedor"): # verifica se o vendedor que listar com qtd menor que 5
            print("1) Filtrar por quantidade menor que 5")
            print("2) Não Filtrar")
            filtrar = input("-> ")
            
        if (livro.nome == nome):
            if (tipo == "operação_cliente"): 
                return livro
            elif (tipo == "operação_vendedor"):
                if (filtrar == 1): # Filtrar = True
                    if (livro.quantidade_em_estoque <= 5): 
                        return livro
                    else:
                        return
                else:
                    return livro
            else:
                print(livro)
                return 
        else:
            print("Livro não encontrado")
            return 0
            
    def consultarPreco(self, maior, menor):
        if (tipo == "operação_vendedor"): 
            print("1) Filtrar por quantidade menor que 5")
            print("2) Não Filtrar")
            filtrar = input("-> ")
        livros = None
        preco = menor
        while (preco != maior):
            livro = Livro.object.get(preco)
            if (tipo == "operação_cliente"):
                livros.append(livro)
            elif (tipo == "operação_vendedor"): 
                if (filtrar == 1):
                    if (livro.quantidade_em_estoque <= 5): 
                        livros.append(livro)
                    else:
                        continue
                else:
                    livros.append(livro)
            else:
                livros.append(livro)
            preco += 0.1
            
        if (livros == none):
            print("não temos livros nessa faixa de valores\n")
            return
        if (tipo == "operação_busca"): # Não é cliente nem vendedor
            print(livros)
            return 
        return livros
    
    def consultarCategoria(self,categoria):
        livro = Livro.object.get(categoria==categoria)
        if (tipo == "operação_vendedor"):
            print("1) Filtrar por quantidade menor que 5")
            print("2) Não Filtrar")
            filtrar = input("-> ")
        if (livro.categoria == categoria):
            if (tipo == "operação_cliente"): 
                return livro
            elif (tipo == "operação_vendedor"): 
                if (filtrar == 1):
                    if (livro.quantidade_em_estoque >= 5): 
                        return livro
                else:
                    return livro
            else:
                livro = Livro.object.get(titulo==nome)
                print(livro)
                return
        else:
            print("Não temos livros dessa categoria")
            
    def ConsultarMari(self):
        livro = Livro.object.get(origem==local)
        if (tipo == "operação_vendedor"): # Vendedor
            print("1) Filtrar por quantidade menor que 5")
            print("2) Não Filtrar")
            filtrar = input("-> ")
            
        if (livro.origem == local):
            if (tipo == "operação_cliente"): 
                return livro
            elif (tipo == "operação_vendedor"):
                if (filtrar == 1):
                    if (livro.quantidade_em_estoque >= 5): 
                        return livro
                else:
                    return livro    
            else:
                livro = Livro.object.get(titulo==nome)
                print(livro)
                return
        else:
            print("Não temos livros de Mari")

