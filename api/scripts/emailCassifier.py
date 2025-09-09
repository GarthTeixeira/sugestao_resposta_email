import pickle
from collections import Counter

class EmailCassifier:
    def __init__(self, model_path: str):
        """Inicializa o classificador de e-mails com modelo pré-treinado"""
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def classificar(self, email_texto):
        """Classifica o e-mail com base nos tokens pré-processados"""
        # Aqui assumimos que o modelo espera uma lista de tokens
        if not self.validar_tamanho_texto(email_texto):
            return "improdutivo"
        
        return self.classificar_fragmentos(email_texto)
    
    def validar_tamanho_texto(self, email_text, max_length=10000):
        """Valida se o texto do e-mail não excede o tamanho máximo"""
        return False if len(email_text) > max_length else True 
    
    def classificar_fragmentos(self, email_text:str):
        """Quebra email em fragmentos e classifica cada um"""
        fragmentos = email_text.split('.')
        fragmentos_classificados = self.model.predict(fragmentos)

        #compara em lista e retorna o mais frequente
        contador = Counter(fragmentos_classificados)
        mais_comum = contador.most_common(1)[0][0] 
        return mais_comum
        
        
       