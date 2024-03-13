import os
from openai import OpenAI

print(os.environ.get("OPENAI_API_KEY"))

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def create_chat_completion(messages, temperature=0.1, response_format={"type": "json_object"}):
    return client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=temperature,
        response_format=response_format
    )