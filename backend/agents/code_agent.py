import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
class CodeAgent:
    def generate_code(self, query:str):
        prompt=f"""
        You are a python developer

        Task:
        {query}

        - Return runnable python code
        - Include imports
        - No explainations
        - No marrkdown
        """

        try: 
            response=client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content":prompt}],
                temperature=0.2
                )
            code=response.choices[0].message.content.strip()
            return code.replace("```python", "").replace("```", "")
        except Exception as e:
            return f"error: {str(e)}"
        
