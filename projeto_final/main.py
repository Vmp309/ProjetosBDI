import psycopg2
from menu_off import MenuOff
from menu_client import MenuClient
from menu_seller import MenuSeller

from gerenciadorBD import GerenciadorBD
from Client import Cliente
from Seller import Vendedor

if __name__ == "__main__":
    conexao = psycopg2.connect(
        database="Reading_Merry",
        user="augusto",
        password="123",
        host="localhost"
    )

gerenciador = GerenciadorBD(conexao)

isClientLogged = False
isSellerLogged = False

cliente = Cliente(cpf=None, username=None, password=None, nome=None, isFlamengo=None, isOnePieceFan=None, isSousa=None, endereco=None)
vendedor = Vendedor(cpf=None, username=None, password=None, nome=None)

while True:
    
    if isClientLogged: # Menu exibido caso o cliente esteja logado
        menu_client = MenuClient(cliente=cliente, gerenciador=gerenciador)
        menu_client.exibir_menu()
        if(menu_client.fez_logout == True):
            cliente = menu_client.cliente
            isClientLogged = False
        
    elif isSellerLogged: # Menu exibido caso o vendedor esteja logado
        menu_seller = MenuSeller(vendedor=vendedor, gerenciador=gerenciador)
        menu_seller.exibir_menu()
        if(menu_seller.fez_logout == True):
            vendedor = menu_seller.vendedor
            isSellerLogged = False
    else: # Menu exibido caso não haja nenhum usuário online
        menu_off = MenuOff(gerenciador=gerenciador)
        menu_off.exibir_menu()
        isSellerLogged = menu_off.vendedor_fez_login
        isClientLogged = menu_off.cliente_fez_login
        if(isClientLogged):
            cliente = menu_off.enviarCliente
        if(isSellerLogged):
            vendedor = menu_off.enviarVendedor        
        
