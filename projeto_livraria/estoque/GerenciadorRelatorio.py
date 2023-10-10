from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO

class GerenciadorRelatorio:
    @classmethod
    def gerar_relatorio_estoque(cls, data):
        # Configure o buffer para armazenar o PDF
        buffer = BytesIO()

        # Crie o objeto PDF com o buffer
        pdf = canvas.Canvas(buffer)

        # Adicione o conteúdo ao PDF
        pdf.drawString(100, 800, "Relatório de Estoque de Livros")

        # Adicione as informações dos livros
        y = 750
        for livro in data:
            pdf.drawString(100, y, f"Título: {livro.titulo}")
            pdf.drawString(100, y - 20, f"Autor: {livro.autor}")
            pdf.drawString(100, y - 40, f"Quantidade em Estoque: {livro.quantidade_em_estoque}")
            y -= 60

        # Salvando o PDF
        pdf.showPage()
        pdf.save()

        # Coloque o buffer na posição 0 e retorne o PDF como uma resposta
        buffer.seek(0)
        response = FileResponse(buffer, as_attachment=True, filename='relatorio_estoque.pdf')

        return response