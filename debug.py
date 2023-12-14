from openai import OpenAI
import yaml
import os

OPENAI_CONFIG = yaml.load(open('config.yaml'), Loader=yaml.FullLoader)
os.environ["OPENAI_API_KEY"] = OPENAI_CONFIG['OPENAI_KEY']

client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    # {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "告诉我你是谁，用中文"}
  ]
)

print(completion.choices[0].message)