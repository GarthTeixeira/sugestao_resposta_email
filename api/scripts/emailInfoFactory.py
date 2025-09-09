
class EmailInfo:
    def __init__(self, autor, remetente, assunto, corpo):
        self.autor = autor
        self.remetente = remetente
        self.assunto = assunto
        self.corpo = corpo
    
    def format_info(self) -> str:
        return f"De: {self.autor} Para: {self.remetente}\nAssunto: {self.assunto}\n\n{self.corpo}"