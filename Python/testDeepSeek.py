from openai import OpenAI
# from config import key_DeepSeek_V3
from config import key_DeepSeek_R1

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=key_DeepSeek_R1,
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-chat",
  messages=[
    {
      "role": "user",
      "content": "Що ти можешь розповісти про себе коротко (напиши свою модель)?"
    }
  ]
)
print(completion.choices[0].message.content)