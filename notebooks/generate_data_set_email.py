import random
import pandas as pd

# Novos exemplos para emails produtivos
produtivo_base_extra = [
    "Gentileza {acao} conforme combinado",
    "Lembrete: {acao} precisa ser feito {prazo}",
    "Não esqueça de {acao} até {prazo}",
    "Favor priorizar {acao} para o projeto",
    "Atualize-nos sobre {acao} assim que possível",
    "Aguardamos {acao} para prosseguir",
    "Reforçando a necessidade de {acao} {prazo}",
    "Solicito urgência em {acao}",
    "Por gentileza, realize {acao} antes do prazo",
    "Informe o andamento de {acao} até {prazo}"
]
produtivo_acao_extra = [
    "preencher o formulário",
    "realizar o backup dos dados",
    "testar a nova funcionalidade",
    "enviar o orçamento",
    "finalizar a análise",
    "compartilhar o relatório",
    "atualizar o cadastro",
    "preparar a apresentação",
    "confirmar a entrega",
    "notificar o cliente"
]
produtivo_prazo_extra = [
    "o quanto antes",
    "até o início da tarde",
    "antes do fechamento",
    "até segunda-feira",
    "até o próximo encontro"
]

# Novos exemplos para emails improdutivos
improdutivo_base_extra = [
    "Espero que todos estejam bem!",
    "Desejo sucesso a todos!",
    "Aproveitem o {evento}!",
    "Que seja um excelente {evento}",
    "Muito obrigado pela atenção",
    "Fico feliz pelo {evento}",
    "Desejo um ótimo dia",
    "Agradeço pela parceria",
    "Tenham um excelente {evento}",
    "Feliz {evento} para todos!"
]
improdutivo_evento_extra = [
    "dia", "semana", "mês", "reunião", "descanso", "almoço", "coffee break"
]
improdutivo_acao_extra = [
    "participação", "dedicação", "atenção", "presença", "contribuição"
]

# Listas de exemplos para cada classe
produtivo_base = [
    "Preciso que você {acao} até {prazo}",
    "Favor {acao} para o cliente",
    "Solicito {acao} imediatamente",
    "Por favor, confirme {acao}",
    "Temos dúvidas sobre {acao}",
    "Necessário {acao} antes de {prazo}",
    "Pode verificar {acao}?",
    "Precisamos de {acao} para continuar",
    "Verifique o status de {acao}",
    "Envie {acao} até {prazo}"
]
produtivo_acao = [
    "atualizar o relatório",
    "resolver o chamado",
    "enviar os documentos pendentes",
    "confirmar a reunião",
    "revisar o contrato",
    "responder à solicitação do cliente",
    "validar os dados do sistema",
    "analisar a proposta",
    "fornecer feedback",
    "agendar reunião"
]
produtivo_prazo = [
    "hoje", "até sexta-feira", "até amanhã", "até o final do dia", "antes de quarta-feira"
]

improdutivo_base = [
    "Parabéns pelo {evento}!",
    "Obrigado por {acao}",
    "Desejo um ótimo {evento}",
    "Agradecemos {acao}",
    "Bom {evento} a todos!",
    "Feliz {evento}!",
    "Agradeço por {acao}",
    "Parabéns pelo excelente trabalho",
    "Obrigado pelo envio de {acao}",
    "Espero que tenha um ótimo {evento}"
]
improdutivo_evento = [
    "aniversário", "fim de semana", "início de semana", "trabalho", "projeto", "feriado", "natal", "ano novo"
]
improdutivo_acao = [
    "ajuda prestada", "colaboração", "compartilhamento dos materiais", "suporte"
]

# Combine all entries
produtivo_base += produtivo_base_extra
produtivo_acao += produtivo_acao_extra
produtivo_prazo += produtivo_prazo_extra

improdutivo_base += improdutivo_base_extra
improdutivo_evento += improdutivo_evento_extra
improdutivo_acao += improdutivo_acao_extra

# Gerar emails
emails = []
labels = []

# Gerar 100 emails produtivos
for _ in range(100):
    base = random.choice(produtivo_base)
    acao = random.choice(produtivo_acao)
    prazo = random.choice(produtivo_prazo)
    email = base.format(acao=acao, prazo=prazo)
    emails.append(email)
    labels.append("produtivo")

# Gerar 100 emails improdutivos
for _ in range(100):
    base = random.choice(improdutivo_base)
    if "{evento}" in base:
        evento = random.choice(improdutivo_evento)
        email = base.format(evento=evento)
    else:
        acao = random.choice(improdutivo_acao)
        email = base.format(acao=acao)
    emails.append(email)
    labels.append("improdutivo")

# Criar DataFrame
df = pd.DataFrame({"email": emails, "label": labels})

# Embaralhar
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Salvar CSV
df.to_csv("notebooks/emails_produtivo_improdutivo.csv", index=False)

print("Dataset gerado com 200 emails e salvo em 'emails_produtivo_improdutivo.csv'")
print(df.head())
