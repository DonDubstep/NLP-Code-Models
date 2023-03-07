import os
import config
import openai
openai.api_key = config.api_key_GPT

prompt= "create an addition function"

response = openai.Completion.create(
  model="code-cushman-001",
  prompt=prompt,
  temperature=0.5,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

print(response.choices[0].text)

