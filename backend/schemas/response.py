from pydantic import BaseModel

class CodeResponse(BaseModel):
    success: bool
    status: str
    final_code: str
    result: dict
    early_stop: bool