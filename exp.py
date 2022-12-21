import os
import openai
OPENAI_API_KEY1="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"
OPENAI_API_KEY="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"
class text_generation:
  def __init__(self):
    openai.api_key =OPENAI_API_KEY
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


