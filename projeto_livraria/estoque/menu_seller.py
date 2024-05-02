from menu_buscar import MenuBuscar

class MenuSeller:
    vendedor_online = True

    def __init__(self):
        pass

    def exibir_menu(self):
        print("Olá, vendedor {nome do carinha}")
        print("O que você gostaria de fazer?")
        print("1) Buscar Livro.")
        print("2) Adicionar Livro.")
        print("3) Remover Livro.")
        print("4) Sair da Conta.")
        opcao = input("Digite a opcao: ")
        if(opcao == 1):
            resultado = MenuBuscar()
            resultado.exibir_menu(1)
        elif(opcao == 2):
            pass # Chama a funcionalidade de adicionar um livro no Banco de Dados
        elif(opcao == 3):
            pass # Chama a funcionalidade de remover um livro no Banco de Dados            
        elif(opcao == 4):
            self.vendedor_online = False # É utilizado para sair do menu do vendedor e ir para o Menu off
        else:
            return