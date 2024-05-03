from Client import Cliente
from menu_busca import MenuBusca

class MenuClient:

    def __init__(self, cliente, gerenciador):
        self.fez_logout = False
        self.cliente = cliente
        self.opcao = 0
        self.gerenciador = gerenciador

    def exibir_menu(self):
        print("\n\n\nOlá " + self.cliente.username + ", seja Bem-Vindo a livraria Reading Merry!")
        print("O que você gostaria de fazer?")
        print("1) Buscar Livro.")
        print("2) Efetuar uma Compra.")
        print("3) Mostrar minhas informações.")
        print("4) Fazer o Logout.")
        self.opcao = input("-> ")
        if self.opcao == "1":
            menu_busca = MenuBusca(self.gerenciador)
            menu_busca.exibir_menu(tipo_operacao="busca_normal")
        elif self.opcao == "2":
            pass # TODO fazer a funcionalidade de compra
        elif self.opcao == "3":
            self.mostrar_info()
        elif self.opcao == "4":
            self.cliente = Cliente(cpf=None, username=None, password=None, nome=None, isFlamengo=None, isOnePieceFan=None, isSousa=None, endereco=None)
            self.fez_logout = True
            print("\n\n\nVocê fez o logout com sucesso!\n")
        
        return



    def mostrar_info(self):
        print("Essas são suas informações:\n")
        if(self.cliente.isSousa):
            print("Nome: " + self.cliente.nome + " de Sousa")
        else:
            print("Nome: " + self.cliente.nome)
        print("Endereço: " +self.cliente.endereco)
        print("CPF: " + self.cliente.cpf + "\n")
        print("Username: " + self.cliente.username)
        print("Password: " + self.cliente.password + "\n")
        print("Torce para o Flamengo: " + str(self.cliente.isFlamengo))
        print("É fã de One Piece: " + str(self.cliente.isOnePieceFan))
        