from .GerenciadorCliente import GerenciadorCliente
from .GerenciadorVendedor import GerenciadorVendedor

def authenticate(username, password, user_type):
    if user_type == 0:
        return GerenciadorCliente.login(username, password)
    
    elif user_type == 1:
        return GerenciadorVendedor.login(username, password)

