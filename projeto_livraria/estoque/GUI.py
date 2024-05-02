from menu_client import MenuClient
from menu_seller import MenuSeller
from menu_off import MenuOff
from Vendas import Vendas

from .models import Cliente 
from .models import Venda
from .models import Livro
from django.db import connection

isClientLogged = False
isSellerLogged = False

while(True):
    if(isClientLogged): # Menu exibido quando o cliente estiver logado
        menu_cliente = MenuClient()
        isClientLogged = menu_cliente.cliente_online
    elif(isSellerLogged): # Menu exibido quando o vendedor estiver logado
        menu_vendedor = MenuSeller()
    else: # Menu exibido quando o usuário não estiver logado
        menu_off = MenuOff()
        menu_off.exibir_menu()
        isClientLogged = menu_off.cliente_fez_login # Se o cliente tiver efetuado o login, a próxima iteração chamará o menu do cliente
        isSellerLogged = menu_off.vendedor_fez_login # Se o vendedor tiver efetuado o login, a próxima iteração chamará o menu do vendedor
