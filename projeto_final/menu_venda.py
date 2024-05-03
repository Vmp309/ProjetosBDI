from Client import Cliente
from Seller import Vendedor
from Venda import Venda
from gerenciadorBD import GerenciadorBD
import datetime

class MenuVenda():
    
    def __init__(self, gerenciador, cliente):
        self.gerenciador = gerenciador
        self.cliente = cliente
        self.vendedor = Vendedor(cpf=None, username=None, password=None, nome=None)
        self.opcao = 0
        self.carrinho = []
        self.valor = 0
        self.valor_com_desconto=0
        self.venda = Venda(self.cliente,self.vendedor,forma_pagamento=None,valor_total=None,valor_desconto=None,livros=[],data=None) 

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
                self.remover_do_carrinho(titulo)
            elif self.opcao == "3":
                self.finalizar_compra()
            elif self.opcao == "4":
                return

        

    def adicionar_ao_carrinho(self, titulo):
        livro_atual= self.gerenciador.buscar_titulo_Livro(titulo)
        if livro_atual == None:
            print("Livro não encontrado!")
            return
        else:
            self.venda.livros.append(livro_atual.id_livro)
            self.carrinho.append(livro_atual)

    def remover_do_carrinho(self, titulo):
        livro_atual= self.gerenciador.buscar_titulo_Livro(titulo)
        if livro_atual == None:
            print("Livro não encontrado!")
            return
        else:
            self.venda.livros.remove(livro_atual.id_livro)

    
    def mostrar_livro(self, livro):
        print("\nID: " + str(livro.id_livro))
        print("Titulo: "+ livro.titulo)
        print("Autor: " + livro.autor)
        print("Fabricado em: " + livro.origem)
        print("Categoria: " + livro.categoria)
        print("Sinopse: "+ livro.sinopse)
        print("Quantidade em Estoque: " + str(livro.quantidade))
        print("Preço: " + str(livro.valor))

    def desconto(self):
        desconto=0.0
        if (self.cliente.isFlamengo ):
            desconto+=0.05
        elif (self.cliente.isOnePieceFan) :
            desconto+=0.05
        elif (self.cliente.isSousa):
            desconto+=0.05
        self.venda.valor_total = self.valor
        self.venda.valor_desconto = self.valor - (self.valor * 0.05)
        
        for livro in self.carrinho:
            self.valor += livro.valor
        print("Valor da compra: " + str(self.valor))
        if (desconto >= 0.0):
            print("Valor com desconto: " + str(self.valor_com_desconto))

    def finalizar_compra(self):

        self.desconto()

        print("Defina a forma de pagamento: ")
        print("1) Cartão.")
        print("2) Boleto.")
        print("3) Pix.")
        print("4) Berries.")
        form_pagamento = input("-> ")
        if form_pagamento == "1":
            form_pagamento = "Cartão"
            print("Pagando com o Cartão")
        elif form_pagamento == "2":
            form_pagamento = "Boleto"
            print("Pagando com Boleto")
        elif form_pagamento == "3":
            form_pagamento = "Pix"
            print("Pagando com Pix")
        elif form_pagamento == "4":
            form_pagamento = "Berries"
            print("Pagando com Berries")
        self.venda.forma_pagamento = form_pagamento
        self.venda.pagamento_concluido = True
        self.venda.data = datetime.date.today() 
        self.gerenciador.adicionar_venda(self.venda)
        


    