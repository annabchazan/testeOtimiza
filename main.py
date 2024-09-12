
import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("A chave de API não foi encontrada. Verifique o arquivo .env.")

# response = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Please list 10 animals."}
#     ]
# )

# print(response.choices[0].message['content'])

openai.api_key = api_key

description = "a baby with an old man's face crying."

response = openai.Image.create(
    prompt=description,
    n=1,  
    size="1024x1024"  
)

image_url = response['data'][0]['url']

print(f"Imagem gerada: {image_url}")
