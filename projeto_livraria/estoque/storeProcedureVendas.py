import django.db
from django.db import connection


CREATE OR REPLACE PROCEDURE gerar_relatório_de_vendas(
    @dataInicio DATE,
    @dataFim DATE
)
AS $$
BEGIN

  -- Declare variables for storing report data
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

  return totalVendas,descontoTotal,totalPago,vendasDinheiro,vendasCartaoDebito,vendasCartaoCredito,vendasBerries,VendasConcluidas

END $$ LANGUAGE plpgsql;
