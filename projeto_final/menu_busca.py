class MenuBusca:

    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.opcao = 0


    def exibir_menu(self, tipo_operacao):
        if tipo_operacao == "busca_normal":
            self.exibir_buscaNormal()
        elif tipo_operacao == "busca_vendedor":
            pass
        elif tipo_operacao == "busca_venda":
            pass


    def exibir_buscaNormal(self):
        print("-----------------------------------\n\n")
        print("1) Buscar Livro por Titulo.")
        print("2) Buscar Livro por Faixa de Preço.")
        print("3) Buscar Livro por Categoria.")
        print("4) Buscar por Local onde o Livro foi produzido.")
        self.opcao = input("-> ")
        if self.opcao == "1":
            titulo = input("Qual é o titulo do Livro? \n-> ")
            livro = self.gerenciador.buscar_titulo_Livro(titulo)
            if livro == None:
                print("Não há nenhum livro com esse título no catalogo")
            else:
                self.mostrar_livro(livro)
        elif self.opcao == "2":
            menor = input("Digite o menor valor\n-> ")
            maior = input("Digite o maior valor\n-> ")
            livros = self.gerenciador.buscar_faixa_preco_Livro(maior, menor)
            if livros == None:
                print("Não há nenhum livro com essa faixa de preço.")
            else:
                for livro in livros:
                    mostrar_livro[livro]
        elif self.opcao == "3":
            pass
        elif self.opcao == "4":
            pass

    def mostrar_livro(self, livro):
        print("ID: " + str(livro.id_livro))
        print("Titulo: "+ livro.titulo)
        print("Autor: " + livro.autor)
        print("Fabricado em: " + livro.origem)
        print("Categoria: " + livro.categoria)
        print("Sinopse: "+ livro.sinopse)
        print("Quantidade em Estoque: " + str(livro.quantidade))
        print("Preço: " + str(livro.valor))


        