import logging
from typing import Protocol
import google.generativeai as genai
from openai import OpenAI
from helpers import layout

client = OpenAI(api_key="")
genai.configure(api_key="")

class IAAPIClient(Protocol):
    def to_ask(self, text) -> str:...

class GeminiApi(IAAPIClient):
    def to_ask(self, text) -> str:
        logging.warning('Calling IA....')
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])
        msg = f"extraia os dados desse texto {text} e altere o valor desse json: {layout}"
        response = chat.send_message(msg)
        json_response = chat.send_message(f"transforme em um json valido: {response.text}")
        return json_response.text

class OpenIAApi(IAAPIClient):
    def to_ask(self, text) -> str:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
        )
        return completion.choices[0].message

    
