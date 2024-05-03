class MenuBusca:

    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.opcao = 0
        self.opcao2 = 0

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
            self.pedir_titulo()
        elif self.opcao == "2":
            self.pedir_faixa()
        elif self.opcao == "3":
            self.pedir_categoria()
        elif self.opcao == "4":
            self.pedir_local()

    def mostrar_livro(self, livro):
        print("ID: " + str(livro.id_livro))
        print("Titulo: "+ livro.titulo)
        print("Autor: " + livro.autor)
        print("Fabricado em: " + livro.origem)
        print("Categoria: " + livro.categoria)
        print("Sinopse: "+ livro.sinopse)
        print("Quantidade em Estoque: " + str(livro.quantidade))
        print("Preço: " + str(livro.valor))

    def pedir_titulo(self):
        titulo = input("Qual é o titulo do Livro? \n-> ")
        livro = self.gerenciador.buscar_titulo_Livro(titulo)
        if livro == None:
            print("Não há nenhum livro com esse título no catalogo")
        else:
            self.mostrar_livro(livro)

    def pedir_faixa(self):
        menor = input("Digite o menor valor\n-> ")
        maior = input("Digite o maior valor\n-> ")
        livros = self.gerenciador.buscar_faixa_preco_Livro(maior, menor)
        if len(livros) == 0:
            print("Não há nenhum livro com essa faixa de preço.")
        else:
            for livro in livros:
                self.mostrar_livro(livro)

    def pedir_categoria(self):
        categoria = input("Digite a categoria\n-> ")
        livros = self.gerenciador.buscar_categoria_Livro(categoria)
        if len(livros) == 0:
            print("Não há livros para essa categoria.")
        else:
            for livro in livros:
                self.mostrar_livro(livro)

    def pedir_local(self):
        local = input("Digite o local onde o livro foi fabricado\n-> ")
        livros = self.gerenciador.buscar_local_Livro(origem)
        if len(livros) == 0:
            print("Não há livros nesse local.")
        else:
            for livro in livros:
                self.mostrar_livro(livro)


    def exibir_buscaVendedor(self):
        print("-----------------------------------\n\n")
        print("Deseja filtrar a busca pelos livros que possuem menos que 5 unidades disponíveis?")
        print("1) Sim.")
        print("2) Não.")
        self.opcao2 = input("-> ")
        if opcao2 == "2":
            self.exibir_buscaNormal()
        elif opcao2 == "1":
            print("------------------------------------------")
            print("Livros com menos de 5 unidades disponiveis")
            print("------------------------------------------\n")
            print("1) Buscar Livro por Titulo. ")
            print("2) Buscar Livro por Faixa de Preço.")
            print("3) Buscar Livro por Categoria.")
            print("4) Buscar por Local onde o Livro foi produzido.")
            self.opcao = input("-> ")
            if self.opcao == "1":
                self.pedir_titulo()
            elif self.opcao == "2":
                self.pedir_faixa()
            elif self.opcao == "3":
                self.pedir_categoria()
            elif self.opcao == "4":
                self.pedir_local()
            else:
                print("Opção inválida")