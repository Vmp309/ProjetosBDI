form .models import Livros

class MenuBuscar:
    
    def exibir_menu(self, tipo );

        print( "           Consulta de livros")
        opcao = input("""
Digite 0 para pesquisar por nome\n
Digite 1 para pesquisar por faixa de preço\n
Digite 2 para pesquisar por categorias\n>
Digite 3 para pesquisar por vindos de Mari\n
""")
        if opcao == 0:
            nome = input( "Digite o nome do livro")
            livro = consultarNome(nome)
            return livro
        elif opcao == 1:
            maior = input("Digite o maior preço\n>")
            menor = input("Digite o menor preço\n>")
            livro = consultarPreco
            return livro
            
        elif opcao == 2:
            categoria = input("Digite a Categoria\n>") 
            consultarCategoria(categoria)
        elif opcao == 3:
            consultarMari()
        else:
    
    
    def consultarNome(self ,nome):
        livro = Livro.get(categoria==nome)
        if tipo == 0:
            return livro
        elif tipo == 1:
            filtrar=input("Digte 1 para filtar por quantidade menor que 5\nDitite 0 para não filtrar\n>)
            if filtrar == 1
                if livro.quantidade_em_estoque =<5: 
                    return livro
            else:
                return livro
        else:
            print(livro)
            
    def consultarPreco(self, maior , menor):
        livros=none
        preco = menor
        while maior !=menor
            livros = Livro.get(preco)
            preco += 0.1
    
    def consultarCategoria(self,categoria):
        livro = Livro.get(categoria==categoria)
        if livro.categoria==categoria:
            if tipo == 0:
                return livro
            elif tipo == 1:
                filtrar=input("Digte 1 para filtar por quantidade menor que 5\nDitite 0 para não filtrar\n>)
                if filtrar == 1
                    if livro.quantidade_em_estoque =< 5: 
                        return livro
                else:
                    return livro
            else:
                livro = Livro.get(titulo==nome)
                print(livro)
        else:
            print("Não temos livros dessa categoria")
    def ConsultarMari(self):
        livro = Livro.get(origem==local)
        if livro.origem==local:
            if tipo == 0:
                return livro
            elif tipo == 1:
                filtrar=input("Digte 1 para filtar por quantidade menor que 5\nDitite 0 para não filtrar\n>)
                if filtrar == 1
                    if livro.quantidade_em_estoque =< 5: 
                        return livro
                else:
                    return livro
            else:
                livro = Livro.get(titulo==nome)
                print(livro)
        else:
            print("Não temos livros de Mari")

    