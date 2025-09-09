# Instale a biblioteca se ainda não tiver
# pip install fpdf

from fpdf import FPDF

# Função para criar PDF
def create_pdf(filename, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)  # multi_cell para quebrar linhas automaticamente
    pdf.output(filename)
    print(f"PDF '{filename}' criado com sucesso!")

# --- Email produtivo ---
email_produtivo = """\
Por favor, confirme sua presença na reunião de amanhã às 10h. 
Traga sugestões para otimizar nossos processos e revisar o planejamento do projeto. 
Precisamos da sua resposta para prosseguir com as ações necessárias.
"""

create_pdf("teste_produtivo.pdf", email_produtivo)

# --- Email improdutivo ---
email_improdutivo = """\
Parabéns pelo excelente trabalho realizado no último trimestre! 
Agradecemos sua colaboração e desejamos um ótimo final de semana para você e sua equipe.
"""

create_pdf("teste_improdutivo.pdf", email_improdutivo)
