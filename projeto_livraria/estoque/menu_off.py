from .models import Cliente
from GerenciadorCliente import GerenciadorCliente

class MenuOff:
    opcao = 99
    cliente_fez_login = False
    vendedor_fez_login = False
    variavel_usuario_login = ''
    
    def __init__(self):
        pass

    def exibir_menu(self):
        print("Olá, seja bem-vindo a biblioteca Reading Merry!")
        print("O que você gostaria de fazer?")
        print("1) Buscar Livros.")
        print("2) Fazer o Login.")
        print("3) Fazer um Registro.")
        print("0) Sair do Programa.")
        opcao = input("Digite a opção: ")
        if(opcao == 1):
            pass # Chama o menu buscar livros
        elif(opcao == 2):
            self.exibir_login() # Exibe a funcionalidade de login
        elif(opcao == 3):
            self.exibir_registro() # Exibe a funcionalidade de registro
        elif(opcao == 0): 
            print("Programa encerrado!\n\n")
            exit(0)
        else:
            return
            
    
    def exibir_login(self):
        cliente = GerenciadorCliente()
        variavel_usuario_login = input("Digite o seu username: ")
        cliente.obter_Cliente(pk="variavel_usuario_login")
        

    def exibir_registro(self):
        pass