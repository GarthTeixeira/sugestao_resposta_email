# ✉️ Projeto de sugestão de resposta de e-mails

Olá este projeto consiste em um classificador de e-mails que também retorna textos sugestivos para resposta dos mesmos. Este guia irá ajudá-lo a configurar e executar o projeto localmente.

## 🛠️ Requisitos

- Conta no Hugging Face
- Python >= 3.12
- Node
- Jupyter notebook

**⚠️ Atenção:** Sempre certifique-se estar executando os comandos a partir da pasta do diretŕoio, caso contrário pode encontrar problemas de caminho de arquivos e módulos.

## 🐍 1. (Opcional) Criar Ambiente Virtual Python 


```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## 📦 2. Instalar Dependências Python

```bash
pip install -r requirements.txt
```

## 📦 3. Instalar Dependências Node.js

```bash
npm install
```

## 🧠 4. Gerar o DataSet

Execute o script responsável pela geração do modelo (ajuste conforme necessário):

```bash
python notebooks/generate_data_set_email.py
```

## 🤖 5. Gerar Modelo

Execute também o modelo com a lib papermill, o modelo é necessário para instalar dependencias importantes caso esteja utilizando-o.

```bash
papermill notebooks/generate_model.ipynb notebooks/modelo_treinado.ipynb --cwd notebooks
```

## 🦚 6. Gerar Estilos

```bash
npm run build:css
```

## 🚀 7. Rodar a Aplicação Localmente

```bash
python api/main.py
```

Pronto! Acesse a aplicação em `http://localhost:5000` (ou conforme configurado).