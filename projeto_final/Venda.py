class Venda:
    def __init__(self, id_venda, cliente, vendedor, forma_pagamento, valor_total, valor_desconto, livros):
        self.id_venda = id_venda
        self.cliente = cliente
        self.vendedor = vendedor
        self.forma_pagamento = forma_pagamento
        self.valor_total = valor_total
        self.valor_desconto = valor_desconto
        self.livros = livros
