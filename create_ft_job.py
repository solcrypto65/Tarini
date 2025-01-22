from openai import OpenAI, OpenAIError
import os
from pathlib import Path

OpenAI.api_key  = 'API-KEY'
client = OpenAI()

model_name = 'gpt-3.5-turbo'
file_id = 'file-SN42WZ5hCKgiZLhWmwzX9b'

response = client.fine_tuning.jobs.create(
                training_file=file_id,
                model=model_name
            )

print(response)   



