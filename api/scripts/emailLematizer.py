import spacy

class EmailLematizer:
 
    def __init__(self, language_model="pt_core_news_sm"):
        """Inicializa o processador de e-mails com modelo de NLP"""
        self.__nlp = spacy.load(language_model)
    
    
    def lemmatize_text(self,text: str) -> str:
        """Lematiza e remove stopwords/pontuações de um texto."""
        doc = self.__nlp(text.lower())
        return " ".join([
            token.lemma_ for token in doc
            if not token.is_punct and not token.is_space and token.text not in self.__nlp.Defaults.stop_words
        ])