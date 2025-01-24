from openai import OpenAI, OpenAIError
import os
from pathlib import Path

OpenAI.api_key = os.getenv('OPENAI-API-KEY')

client = OpenAI()
response = client.files.create(
                file=Path('ft_messages.jsonl'),
                purpose='fine-tune'
            )

print(response)   

