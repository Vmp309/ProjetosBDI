from menu_buscar import MenuBuscar

class MenuClient:
    opcao = 99
    cliente_online = True
    lista_compra = []   

    def __init__(self):
        pass

    def exibir_menu(self):
        print("Olá {Nome do carinha}, seja bem-vindo a biblioteca Reading Merry!")
        print("O que você gostaria de fazer?")
        print("1) Buscar Livros.")
        print("2) Iniciar uma Compra.")
        print("3) Editar Perfil.")
        print("4) Sair da Conta.")
        opcao = input("Digite a opção: ")
        if(opcao == 1): # Chama o menu de busca apenas para printar o livro
            resultado = MenuBuscar()
            resultado.exibir_menu(3)
        elif(opcao == 2):
            pass # Efetua a funcionalidade de compra.
        elif(opcao == 3):
            pass # Efetua a edição dos dados do cliente
        elif(opcao == 4):
            self.cliente_online = False # É utilizado para sair do menu cliente e ir para o Menu off
        else: 
            return


            