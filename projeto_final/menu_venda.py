from Client import Cliente
from Seller import Vendedor
from gerenciadorBD import GerenciadorBD

class MenuVenda():
    
    def __init__(self, gerenciador, cliente):
        self.gerenciador = gerenciador
        self.cliente = cliente
        self.vendedor = Vendedor(cpf=None, username=None, password=None, nome=None)
        self.opcao = 0
        self.carrinho = []
        self.valor = 0

    def exibir_menu(self):
        vendedores = self.gerenciador.mostrar_vendedores()
        for vendedor in vendedores:
            self.gerenciador.mostrar_vendedor(vendedor)
        user_vendedor = input("Escolha o vendedor que deve concluir a venda\n(Username)-> ")
        if(self.gerenciador.verificar_user_Vendedor(user_vendedor)):
            self.vendedor = self.gerenciador.retornar_vendedor(user_vendedor)
            self.exibir_menu2()
        else:
            print("Acho que você digitou errado...")

    def exibir_menu2(self):
        while (True):
            print("----- Vendedor: " + self.vendedor.username + "-----\n")
            print("Carrinho: ")
            for livro in self.carrinho:
                self.mostrar_livro(livro)
            print("1) Adicionar livro no carrinho.")
            print("2) Remover livro do carrinho.")
            print("3) Comprar.")
            print("4) Cancelar compra.")
            self.opcao = input("-> ")
            if self.opcao == "1":
                titulo = input("Digite o titulo do livro a ser adicionado ao carrinho.\n-> ")
                self.adicionar_ao_carrinho(titulo)
            elif self.opcao == "2":
                pass
            elif self.opcao == "3":
                pass
            elif self.opcao == "4":
                pass

        

    def adicionar_ao_carrinho(self, titulo):
        if self.gerenciador.buscar_titulo_Livro(titulo) == None:
            print("Livro não encontrado!")
            return
        else:
            self.carrinho.append(self.gerenciador.buscar_titulo_Livro(titulo))

    def mostrar_livro(self, livro):
        print("\nID: " + str(livro.id_livro))
        print("Titulo: "+ livro.titulo)
        print("Autor: " + livro.autor)
        print("Fabricado em: " + livro.origem)
        print("Categoria: " + livro.categoria)
        print("Sinopse: "+ livro.sinopse)
        print("Quantidade em Estoque: " + str(livro.quantidade))
        print("Preço: " + str(livro.valor))


    def finalizar_compra(self):
        for livro in self.carrinho:
            self.valor += livro.valor
        print("Valor da compra: " + self.valor)
        print("Defina a forma de pagamento: ")
        print("1) Cartão.")
        print("2) Boleto.")
        print("3) Pix.")
        print("4) Berries.")
        form_pagamento = input("-> ")
        if form_pagamento == "1":
            form_pagamento = "Cartão"
        elif form_pagamento == "2":
            form_pagamento = "Boleto"
        elif form_pagamento == "3":
            form_pagamento = "Pix"
        elif form_pagamento == "4":
            form_pagamento = "Berries"
        

