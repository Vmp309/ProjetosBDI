# para execultar o venv
#  source .venv/bin/activate

# para execultar o projeto
#   python3 manage.py runserver
  
#atualixar as dependencias    
#  pip freeze > requiments.txt 
#instalar as dependencias
#  pip install -r requiments.txt
 
 


# Especificações:
# O objetivo deste estender o sistema anterior para incorporar um módulo de vendas é projetar um
# sistema de vendas. 
# Na parte 1, foi abordado o crud de uma entidade cliente/estoque/venda. 
# Na parte 2, será necessário ter todas as entidades e relacionamentos de um sistema de vendas.

# Um cliente pode realizar várias compras no sistema.
# E cada compra possui um ou mais itens. 
# Para navegar no sistema não é necessário fazer compra ou está logado. 
# Mas na hora de realizar uma compra devem ser informados os dados do cliente.

# Um cliente deve poder verificar o seus dados cadastrais como também os pedidos já realizados.
# Uma compra é efetivada sempre por um vendedor. 
# E possui uma forma de pagamento associada. 
# Se for cartão, boleto, pix ou berries, o pagamento tem um status de confirmação associado.
# Clientes que torcem flamengo, assistem one piece e/ou são de sousa possuem desconto nas
# compras.

# Caso o produto não tenha mais estoque, uma compra não deve ser efetivada.
# Deve ser possivel verificar produtos por nome, faixa de preço, categoria e se foram fabricados em
# Mari. Caso seja um funcionário usando o sistema, ele deve poder filtrar pelos produtos que possuem
# menos que 5 unidades disponíveis.

# Deve ser emitido mensalmente um relatório com as vendas de cada vendedor
# Devem haver pelo menos uma view e uma stored procedure. Também devem ser criados índices e
# restrições de integridade referencial para as tabelas.
