import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class LLMWrapper:
    def __init__(self):
        self.client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model=os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def __call__(self, prompt:str)->str:
        response=self.client.chat.completions.create(
            model=self.model,
            messages=[
            {"role": "system", "content": "You are a senior Python engineer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()   
    