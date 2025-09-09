import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="cerebras",
    api_key= os.getenv("HF_API_TOKEN")
)

email = """Prezado Sr. Silva,
Gostaria de agendar uma reunião para discutir o andamento do projeto. Por favor, informe sua disponibilidade para esta semana.
Atenciosamente,
João"""

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": f"O email a seguir requer uma resposta profissional com no máximo 300 caracteres:\n\n{email}\n\nSugira uma resposta:",
        }
    ],
)

print(completion.choices[0].message)
print(completion.choices[0].message.content)