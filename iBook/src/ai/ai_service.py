import os
from openai import OpenAI

from iBook.src.localization import get_text

class AIException(Exception):
    ...

class AIAssistant(): 
    client = None
    def __init__(self):
        try:
            self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        except:
            raise AIException(get_text("NOT_INITIALIZED_AI_CLIENT"))

    def create_chat_completion(self, messages, temperature=0.1, response_format={"type": "json_object"}):
        return self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=temperature,
            response_format=response_format
    )