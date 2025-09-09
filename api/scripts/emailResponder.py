from huggingface_hub import InferenceClient

class EmailResponder:
    def __init__(self, provieder: str, api_key: str):

        if not provieder:
            raise ValueError("Sem provedor especificado.")
        if not api_key:
            raise ValueError("Sem chave de API especificada.")
        
        self.__client = InferenceClient(
            provider=provieder,
            api_key=api_key
        )

    def classificar(self, texto: str, model:str) -> str:
        """Classifica o e-mail com base nos tokens pré-processados"""
        prompt = f"O email a seguir é produtivo (requere ação imiediata/resposta/operação/suporte técnico/dúvidas/casos em agerto)"
        prompt += " ou improdutivo (sem ação imiediata/social/informativo/felicitações/agradecimentos)?\n\n{texto}\n\nResponda apenas com 'produtivo' ou 'improdutivo', apenas uma dessas duas palavras."
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],  
        }

        resposta = self.gerar_resposta(payload)

        if "produtivo" in resposta.lower():
            return "produtivo"
        else:
            return "improdutivo"
        
       
    def sugerir_resposta(self, email: str, classificacao: str, model:str) -> str:
        """Gera uma sugestão de resposta usando a Hugging Face API."""

        if classificacao == "produtivo":
            prompt = f"O email a seguir requer uma resposta profissional com no máximo 300 caracteres:\n\n{email}\n\nSugira uma resposta:"
        else:
            prompt = f"O email a seguir é social/informativo:\n\n{email}\n\nSugira uma resposta curta e simpática:"

        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],  
        }

        return self.gerar_resposta(payload)
    
    def gerar_resposta(self, payload: dict) -> str:
        """Gera uma resposta usando a Hugging Face API."""
        completition = self.__client.chat.completions.create(**payload)

        if completition is None or not completition.choices:
            raise ValueError("Nenhuma resposta gerada pela API.")
        
        return completition.choices[0].message.content