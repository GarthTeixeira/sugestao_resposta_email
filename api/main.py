import os
import sys
sys.path.append(os.path.dirname(__file__))

from pathlib import Path

# Adiciona o diretório raiz do projeto ao sys.path
project_root = Path(__file__).parent.parent  # ou Path.cwd() se estiver no notebook
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from flask import Flask, request, render_template, redirect, url_for, flash, session
from scripts.emailProcessor import EmailProcessor
from scripts.emailCassifier import EmailCassifier
from scripts.emailResponder import EmailResponder
from scripts.emailInfoFactory import EmailInfo
from dotenv import load_dotenv

import secrets

# Carrega variáveis do arquivo .env
load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = secrets.token_hex(16)

processor = EmailProcessor()
#Para usar o classificador local, descomente a linha abaixo
model_path = project_root / "models" / "email_classifier_pt.pkl"
#classifier = EmailCassifier(model_path=str(model_path))
responder = EmailResponder(provieder="fireworks-ai", api_key=os.environ.get("HF_API_TOKEN"))

inicial_model = "openai/gpt-oss-120b" 

@app.route("/")
def home():
    return redirect(url_for("formulario"))

@app.route("/email_form", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        autor = request.form.get("autor")
        assunto = request.form.get("assunto")
        remetente = request.form.get("remetente")
        tipo = request.form.get("modo")
        
        print(f"Modo: {tipo}")
        print(f"Autor: {autor}")
        print(f"Assunto: {assunto}")
        print(f"Remetente: {remetente}")
        
        texto_pre_processado = None

        if tipo == 'upload' and 'arquivo' in request.files:
            arquivo = request.files.get("arquivo")
            print(f"Arquivo: {arquivo}")
            texto_pre_processado = processor.pre_processar_upload(arquivo)
        elif tipo == 'message' and 'mensagem' in request.form:
            mensagem = request.form.get("mensagem")
            print(f"Mensagem: {mensagem}")
            texto_pre_processado = processor.pre_processar_texto(mensagem)
        else:
            raise Exception('Modo inconpativel:')

        categoria = None
        if texto_pre_processado:
            categoria = responder.classificar(texto_pre_processado, inicial_model)
            # Para usar o classificador local, descomente a linha abaixo e comente a de cima
            #categoria = classifier.classificar(texto_pre_processado)
            
        email_info = EmailInfo(
                autor=autor,
                remetente=remetente,
                assunto=assunto,
                corpo=texto_pre_processado
            ).format_info()
        
        session['resposta_sugerida'] = responder.sugerir_resposta(email_info, categoria, inicial_model)
        session['email_categoria'] = categoria
        
        return redirect(url_for("resposta"))
    

    return render_template("formulario.html")

@app.route("/email_answer")
def resposta():
    resposta =  session.get("resposta_sugerida", "Ainda não existe resposta.")
    categoria = session.get("email_categoria", "indefinida")
    
    return render_template("resposta.html", resposta=resposta, classificacao=categoria.capitalize())

if __name__ == '__main__':
    app.run(debug=True)
