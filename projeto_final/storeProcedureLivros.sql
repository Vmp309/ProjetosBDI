
CREATE OR REPLACE PROCEDURE gerar_relatorio_livros(@dataInicio DATE,@dataFim DATE)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Declarar variáveis ​​para dados de relatório
    DECLARE totalLivros INT := 0;
    DECLARE valorTotalEstoque NUMERIC(10,2) := 0;
    DECLARE livrosPorAutor RECORD SET;

    --Selecionar e agregar dados do livro
    SELECT
        COUNT(*) AS totalLivros,
        SUM(quantidade_em_estoque * valor) AS valorTotalEstoque,
        autor,
        COUNT(*) AS total_livros_por_autor
    FROM Livro
    GROUP BY autor;

    -- Atribuir valores agregados às variáveis
    SET totalLivros = COALESCE(totalLivros, 0);
    SET valorTotalEstoque = COALESCE(valorTotalEstoque, 0);

    --Exibir cabeçalho do relatório
    RAISE NOTICE 'Relatório de Livros';
    RAISE NOTICE '-----------------------';

    -- Exibir o total de livros e o valor total do estoque
    RAISE NOTICE 'Total de Livros: %d', totalLivros;
    RAISE NOTICE 'Valor Total do Estoque: R$%.2f', valorTotalEstoque;

    -- Exibir livros por autor (se houver)
    IF FOUND THEN
        LOOP
            FETCH NEXT FROM livrosPorAutor INTO ROW;
            RAISE NOTICE '-----------------------';
            RAISE NOTICE 'Autor: %s', ROW.autor;
            RAISE NOTICE 'Total de Livros: %d', ROW.total_livros_por_autor;
        END LOOP;
    ELSE
        RAISE NOTICE 'Nenhum livro encontrado.';
    END IF;

    RAISE NOTICE '-----------------------';
END $$;
