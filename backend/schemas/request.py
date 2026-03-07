from pydantic import BaseModel

class CodeRequest(BaseModel):
    code:str
    max_iterations:int=3
    language: str="python"