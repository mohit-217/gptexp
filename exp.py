import os
import openai

class text_generation:
  def __init__(self,openai_api_key):
    openai.api_key =openai_api_key
  def gen_text(self,prompt1):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt1,
    temperature=0,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    
    )
    return response['choices'][0]['text']


