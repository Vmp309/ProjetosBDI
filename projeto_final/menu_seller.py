from Livro import Livro
from Seller import Vendedor

class MenuSeller:

    def __init__(self, vendedor, gerenciador):
        self.fez_logout = False
        self.vendedor = vendedor
        self.opcao = 0
        self.gerenciador = gerenciador

    def exibir_menu(self):
        print("\n\n\nOlá " + self.vendedor.nome)
        print("O que deseja fazer?")
        print("1) Buscar Livro.")
        print("2) Adicionar Livro.")
        print("3) Mostrar minhas informações. ")
        print("4) Fazer o Logout.")
        self.opcao = input("-> ")
        if self.opcao == "1":
            menu_busca = MenuBusca(self.gerenciador)
            menu_busca.exibir_menu(tipo_operacao="busca_vendedor")
        elif self.opcao == "2":
            self.adicionar_livro()
        elif self.opcao == "3":
            self.mostrar_info()
        elif self.opcao == "4":
            self.vendedor = Vendedor(cpf=None, username=None, password=None, nome=None)
            self.fez_logout = True
            print("\n\n\nVocê fez o logout com sucesso!\n")
        
        return


    def adicionar_livro(self):
        id_livro = input("Digite um identificador para o livro.\n->")
        if self.gerenciador.verificar_id_Livro(id_livro) == True:
            print("Já existe um livro com esse id.")
            return
        titulo = input("Digite o titulo do livro.\n-> ")
        if self.gerenciador.verificar_titulo_Livro(titulo) == True:
            print("Já existe um livro com esse titulo.")
            return
        autor = input("Digite o nome do autor do livro.\n-> ")
        origem = input("Digite onde o livro foi produzido.\n-> ")
        categoria = input("Digite a categoria do livro.\n-> ")
        sinopse = input("Digite a sinopse do livro.\n-> ")
        quantidade = int(input("Digite a quantidade de exemplares.\n-> "))
        valor = float(input("Digite o preco do livro.\n-> "))
        livro = Livro(id_livro=id_livro, titulo=titulo, autor=autor, origem=origem, categoria=categoria, sinopse=sinopse, quantidade=quantidade, valor=valor)
        self.gerenciador.adicionar_livro(livro)
        print("Livro adicionado com sucesso!")

    def mostrar_info(self):
        print("Essas são suas informações:\n")
        print("Nome: " + self.vendedor.nome)
        print("CPF: " + self.vendedor.cpf + "\n")
        print("Username: " + self.vendedor.username)
        print("Password: " + self.vendedor.password + "\n")

