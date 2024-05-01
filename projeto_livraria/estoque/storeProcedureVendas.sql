
CREATE OR REPLACE PROCEDURE gerar_relatório_de_vendas(@dataInicio DATE,@dataFim DATE)
LANGUAGE 'plpgsql'
AS $$
BEGIN

  -- Declarar variáveis ​​para armazenar dados de relatório
  DECLARE totalVendas NUMERIC(10,2) := 0;
  DECLARE descontoTotal NUMERIC(10,2) := 0;
  DECLARE totalPago NUMERIC(10,2) := 0;
  DECLARE vendasDinheiro NUMERIC(10,2) := 0;
  DECLARE vendasCartaoDebito NUMERIC(10,2) := 0;
  DECLARE vendasCartaoCredito NUMERIC(10,2) := 0;
  DECLARE vendasPix NUMERIC(10,2) := 0;
  DECLARE vendasBerries NUMERIC(10,2) := 0;
  DECLARE VendasConcluidas INT := 0;

  -- Selecione e agregue dados de vendas dentro do intervalo de datas especificado
  SELECT
    SUM(valorTotal) AS totalVendas,
    SUM(valorDesconto) AS descontoTotal,
    SUM(valorTotal - valorDesconto) AS totalPago,
    CASE WHEN formaPagamento = 'dinheiro' THEN SUM(valorTotal - valorDesconto) ELSE 0 END AS vendasDinheiro,
    CASE WHEN formaPagamento = 'pix' THEN SUM(valorTotal - valorDesconto) ELSE 0 END AS vendasDinheiro,
    CASE WHEN formaPagamento = 'debito' THEN SUM(valorTotal - valorDesconto) ELSE 0 END AS vendasCartaoDebito,
    CASE WHEN formaPagamento = 'credito' THEN SUM(valorTotal - valorDesconto) ELSE 0 END AS vendasCartaoCredito,
    CASE WHEN formaPagamento = 'berries' THEN SUM(valorTotal - valorDesconto) ELSE 0 END AS vendasBerries,
    COUNT(*) AS VendasConcluidas
  FROM Venda
  WHERE Pagconcluido = TRUE
    AND data_venda BETWEEN @dataInicio AND @dataFim;

  -- Atribuir valores agregados às variáveis
  SET totalVendas = COALESCE(totalVendas, 0);
  SET descontoTotal = COALESCE(descontoTotal, 0);
  SET totalPago = COALESCE(totalPago, 0);
  SET vendasDinheiro = COALESCE(vendasDinheiro, 0);
  SET vendasCartaoDebito = COALESCE(vendasCartaoDebito, 0);
  SET vendasCartaoCredito = COALESCE(vendasCartaoCredito, 0);
  SET vendasBerries = COALESCE(vendasBerries, 0);
  SET VendasConcluidas = COALESCE(VendasConcluidas, 0);

  -- Exibir o relatório de vendas
  RAISE NOTICE 'Relatório de Vendas';
  RAISE NOTICE '-----------------------';
  RAISE NOTICE 'Data de Início: %s', @dataInicio;
  RAISE NOTICE 'Data de Fim: %s', @dataFim;
  RAISE NOTICE '-----------------------';
  RAISE NOTICE 'Total de Vendas: R$%.2f', totalVendas;
  RAISE NOTICE 'Total de Descontos: R$%.2f', descontoTotal;
  RAISE NOTICE 'Total Pago: R$%.2f', totalPago;
  RAISE NOTICE 'Vendas em Dinheiro: R$%.2f', vendasDinheiro;
  RAISE NOTICE 'Vendas em Pix: R$%.2f', vendasPix;
  RAISE NOTICE 'Vendas em Cartão de Debito: R$%.2f', vendasCartaoDebito;
  RAISE NOTICE 'Vendas em Cartão de Credito: R$%.2f', vendasCartaoCredito;
  RAISE NOTICE 'Vendas em Berries: R$%.2f', vendasBerries;
  RAISE NOTICE 'Vendas Concluídas: %d', VendasConcluidas;
  RAISE NOTICE '-----------------------';
END $$;