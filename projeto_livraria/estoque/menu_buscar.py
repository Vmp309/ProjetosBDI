form .models import Livros

class MenuBuscar:
    
    def exibir_menu(self, tipo );
        while true:
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
                livro = consultarPreco(maior,menor)
                if livros != none:
                    return livros
                else:
                    return
                
            elif opcao == 2:
                categoria = input("Digite a Categoria\n>") 
                livros = consultarCategoria(categoria)
                if livros != none:
                    return livros
                else:
                    return
            elif opcao == 3:
                livros = consultarMari()
                if livros != none:
                    return livros
                else:
                    return
            else:
                print("opção invalida!\n")
    
    
    def consultarNome(self ,nome):
        livro = Livro.get(categoria==nome)
        if livro.nome == nome:
            if tipo == 0:
                return livro
            elif tipo == 1:
                filtrar=input("Digte 1 para filtar por quantidade menor que 5\nDitite 0 para não filtrar\n>")
                if filtrar == 1
                    if livro.quantidade_em_estoque =<5: 
                        return livro
                else:
                    return livro
            else:
                print(livro)
                return 
        else:
            print("LIvro não encontrado")
            return 0
            
    def consultarPreco(self, maior , menor):
        if tipo == 1:
            filtrar=input("Digte 1 para filtar por quantidade menor que 5\nDitite 0 para não filtrar\n>)
        livros=none
        preco = menor
        while maior !=menor
            livros = Livro.get(preco)
            if tipo == 0:
                livros.append(livro)
            elif tipo == 1:
                if filtrar == 1
                    if livro.quantidade_em_estoque =< 5: 
                        livros.append(livro)
                else:
                    livros.append(livro)
            else:
                livros.append(livro)
            preco += 0.1
            
        if livros == none:
            print("não temos livros nessa faixa de valores\n")
            return
        if tipo > 1:
            return 
        return livros
    
    def consultarCategoria(self,categoria):
        livro = Livro.get(categoria==categoria)
        if tipo == 1:
            filtrar=input("Digte 1 para filtar por quantidade menor que 5\nDitite 0 para não filtrar\n>)
        if livro.categoria==categoria:
            if tipo == 0:
                return livro
            elif tipo == 1:
                if filtrar == 1
                    if livro.quantidade_em_estoque =< 5: 
                        return livro
                else:
                    return livro
            else:
                livro = Livro.get(titulo==nome)
                print(livro)
                return
        else:
            print("Não temos livros dessa categoria")
            
    def ConsultarMari(self):
        livro = Livro.get(origem==local)
        if tipo == 1:
            filtrar=input("Digte 1 para filtar por quantidade menor que 5\nDitite 0 para não filtrar\n>)
            
        if livro.origem==local:
            if tipo == 0:
                return livro
            elif tipo == 1:
                if filtrar == 1
                    if livro.quantidade_em_estoque =< 5: 
                        return livro
                else:
                    return livro
            else:
                livro = Livro.get(titulo==nome)
                print(livro)
                return
        else:
            print("Não temos livros de Mari")

