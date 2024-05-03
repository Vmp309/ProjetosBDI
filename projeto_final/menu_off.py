from gerenciadorBD import GerenciadorBD
from Seller import Vendedor
from Client import Cliente

from menu_busca import MenuBusca

class MenuOff:


    def __init__(self, gerenciador):
        self.fim_do_programa = False
        self.opcao = 0
        self.gerenciador = gerenciador
        self.cliente_fez_login = False
        self.vendedor_fez_login = False
        self.enviarCliente = Cliente(cpf=None, username=None, password=None, nome=None, isFlamengo=None, isOnePieceFan=None, isSousa=None, endereco=None)
        self.enviarVendedor = Vendedor(cpf=None, username=None, password=None, nome=None)


    def exibir_menu(self):
        print("\n\n\n\nOlá, seja bem-vindo ao Reading Merry!")
        print("O que você deseja fazer?")
        print("1) Buscar Livro.")
        print("2) Fazer Login.")
        print("3) Fazer Registro.")
        print("4) Sair do Programa")
        self.opcao = input("-> ")

        if self.opcao == "1":
            menu_busca = MenuBusca(self.gerenciador)
            menu_busca.exibir_menu(tipo_operacao="busca_normal")
        elif self.opcao == "2":
            self.fazer_login() 
        elif self.opcao == "3":
            self.fazer_registro()
        elif self.opcao == "4":
            exit(0)
        else:
            print("\nOpcao invalida!\n\n")



    def fazer_login(self):
        print("\n\n\n\n\n\n\n")
        print("Qual tipo de usuário você quer ser?")
        print("1) Cliente")
        print("2) Vendedor")
        self.opcao = input("-> ")

        if self.opcao == "1": # Faz o login do cliente
            login = input("Digite o seu nome de usuario:\n-> ")
            senha = input("Digite sua senha:\n-> ")
            
            if(self.gerenciador.verificar_user_Cliente(login) == True):
                if(self.gerenciador.verificar_senha_Cliente(login, senha) == True):
                    self.enviarCliente = self.gerenciador.client_para_login(login, senha)
                    self.cliente_fez_login = True
                else:
                    print("Senha incorreta!")
            else:
                print("Nome de usuário do cliente não encontrado!")

        elif self.opcao == "2": # Faz o login do vendedor
            login = input("Digite o seu nome de usuario:\n-> ")
            senha = input("Digite sua senha:\n-> ")
            
            if(self.gerenciador.verificar_user_Vendedor(login) == True):
                if(self.gerenciador.verificar_senha_Vendedor(login, senha) == True):
                    self.enviarVendedor = self.gerenciador.vendedor_para_login(login, senha)
                    self.vendedor_fez_login = True
                else:
                    print("Senha incorreta!")
            else:
                print("Nome de usuário do vendedor não encontrado!")
        else:
            print("\nOpcao invalida!\n\n")
        

    def fazer_registro(self):
        print("\n\n\n\n\n\n\n")
        print("Qual tipo de registro você quer executar?")
        print("1) Cliente")
        print("2) Vendedor")
        self.opcao = input("-> ")
        if self.opcao == "1": # Faz o registro de um cliente
            cpf = input("Digite seu cpf (xxx.xxx.xxx-xx)\n-> ")
            username = input("Digite seu username\n-> ")
            password = input("Digite sua senha\n-> ")
            nome = input("Digite seu nome\n-> ")
            print("Você torce para o Flamengo?")
            print("1) Sim")
            print("2) Não")
            isFlamengo = input("-> ")
            if isFlamengo == "1":
                isFlamengo = True
            if isFlamengo == "2":
                isFlamengo = False

            print("Você é Fã de One Piece?")
            print("1) Sim")
            print("2) Não")
            isOnePieceFan = input("-> ")
            if isOnePieceFan == "1":
                isOnePieceFan = True
            if isOnePieceFan == "2":
                isOnePieceFan = False

            print("Você faz parte dos D. Sousa?")
            print("1) Sim")
            print("2) Não")
            isSousa = input("-> ")
            if isSousa == "1":
                isSousa = True
            if isSousa == "2":
                isSousa = False
            
            endereco = input("Digite seu endereco\n-> ")

            if(self.gerenciador.verificar_cpf_Cliente(cpf) == False):
                if(self.gerenciador.verificar_user_Cliente(username) == False):
                    cliente = Cliente(cpf=cpf, username=username, password=password, nome=nome, isFlamengo=isFlamengo, isOnePieceFan=isOnePieceFan, isSousa=isSousa, endereco=endereco)
                    self.gerenciador.adicionar_cliente(cliente)
                    print("O Registro foi concluído com sucesso!")
                else:
                    print("Já existe um cliente com esse username!")
            else:
                print("Já existe um cliente com esse cpf!")        
             
        elif self.opcao == "2": # Faz o registro de um Vendedor
            cpf = input("Digite seu cpf (xxx.xxx.xxx-xx)\n-> ")
            username = input("Digite seu username\n-> ")
            password = input("Digite sua senha\n-> ")
            nome = input("Digite seu nome\n-> ")
            if(self.gerenciador.verificar_cpf_Vendedor(cpf) == False):
                if(self.gerenciador.verificar_user_Vendedor(username) == False):
                    vendedor = Vendedor(cpf=cpf, username=username, password=password, nome=nome)
                    self.gerenciador.adicionar_vendedor(vendedor)
                    print("O Registro foi concluído com sucesso!")
            else:
                print("Já existe um vendedor com esse cpf!")
            
        else:
            print("\nOpcao invalida!\n\n")