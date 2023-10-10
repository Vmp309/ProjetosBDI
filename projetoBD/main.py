import psycopg2
from  gerenciadorEstoque import GerenciadorEstoque
from livro import Livro
from gerenciadorRelatorio import GerenciadorRelatorio

if __name__ == "__main__":
    conexao = psycopg2.connect(
        database="bookProject",
        user="victoria",
        password="victoria",
        host="localhost"
    )

    gerenciador = GerenciadorEstoque(conexao)
    gerador_relatorio = GerenciadorRelatorio()

    while True:
        print("\nOpções:")
        print("1 - Adicionar livro")
        print("2 - Buscar livro por título")
        print("3 - Listar todos os livros")
        print("4 - Excluir livro por titulo")
        print("5 - Gerar relatório em PDF")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            quantidade = int(input("Digite a quantidade de exemplares: "))
            preco = float(input("Digite o preço do exemplar:"))
            sinopse = input("Inclua a sinopse do livro: ")
            livro = Livro(titulo, autor, quantidade, preco, sinopse)
            gerenciador.adicionar_livro(livro)
            print("Livro adicionado com sucesso!")

        elif opcao == "2":
            titulo = input("Digite o título do livro a ser buscado: ")
            livro = gerenciador.buscar_livro(titulo)
            if livro:
                print(f"Encontrado: {livro.titulo} de {livro.autor}, Quantidade: {livro.quantidade}, Preço: {livro.preco},\n Sinopse: {livro.sinopse}")
            else:
                print("Livro não encontrado.")

        elif opcao == "3":
            livros = gerenciador.listar_livros()
            if livros:
                print("\nLista de Livros:")
                for livro in livros:
                    print(f"{livro.titulo} de {livro.autor}, Quantidade: {livro.quantidade}, Preço: {livro.preco},\n Sinopse: {livro.sinopse}")
            else:
                print("Nenhum livro cadastrado.")

        elif opcao=="4":
            titulo = input("Digite o título do livro a ser excluído: ")
            gerenciador.excluir_livro(titulo)

        elif opcao=="5":
            livros = gerenciador.listar_livros()
            gerador_relatorio.gerar_relatorio_estoque(livros)

        elif opcao == "6":
            conexao.close()
            break

        else:
            print("Opção inválida. Tente novamente.")