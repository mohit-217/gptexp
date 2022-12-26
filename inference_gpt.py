import openai
import os
import openai
class text_generation:
    def __init__(self,openai_api_key,fine_tuned_model_name):
        openai.api_key =openai_api_key
        self.FINE_TUNED_MODEL=fine_tuned_model_name
    def gen_text(self,prompt1):
        response=openai.Completion.create(
            model=self.FINE_TUNED_MODEL,
            temperature=0.7,
            max_tokens=1600,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
            stop=None,
            n=1,
            stream=False,
            prompt=prompt1
        )

        return response['choices'][0]['text']   