import io
import pdfplumber
import re
from werkzeug.datastructures import FileStorage

class EmailProcessor:
    def __init__(self):
        """Inicializa o processador de e-mails com modelo de NLP"""
        pass


    def _limpar_texto(self, texto: str):
        """Remove caracteres especiais e múltiplos espaços"""
        texto = re.sub(r'\s+', ' ', texto)
        # remove carecetes não imprimiveis
        return texto.strip()

    def _ler_txt(self, file: FileStorage):
        """Lê e retorna conteúdo de um TXT vindo de upload"""
        return file.stream.read().decode("utf-8")

    def _ler_pdf(self, file: FileStorage):
        """Lê e retorna conteúdo de um PDF vindo de upload"""
        texto = ""
        # usar BytesIO porque PyPDF2 espera um arquivo binário
        pdf_stream = io.BytesIO(file.stream.read())
        with pdfplumber.open(pdf_stream) as pdf:
            for pagina in pdf.pages:
                texto += pagina.extract_text() + "\n"
        return texto

    def pre_processar_upload(self, file: FileStorage):
        """Detecta extensão do arquivo enviado e retorna texto + tokens"""
        extensao = file.filename.lower().split(".")[-1]
        
        if extensao == "txt":
            texto = self._ler_txt(file)
        elif extensao == "pdf":
            texto = self._ler_pdf(file)
        else:
            raise ValueError("Formato não suportado. Use .txt ou .pdf")
        
        return self._limpar_texto(texto)
    
    def pre_processar_texto(self, texto: str):
        """Processa texto puro (não de upload)"""
        return self._limpar_texto(texto)
