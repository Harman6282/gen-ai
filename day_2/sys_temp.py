import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt = "suggest me a name for a restaurant, only one name"
message_system = {"role": "system", "content": "you are a senior chef"} # system message 
message = {"role": role, "content": prompt}

messages = [message_system, message]

response = client.chat.completions.create( messages=messages, model=model, temperature=2)
print(response.choices[0].message.content)
