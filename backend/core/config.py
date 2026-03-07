from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEBUG : bool=False
    MAX_ITERATIONS : int=3
    EXECUTION_TIMEOUT : int=15
    DATABASE_URL : str="sqlite:///./debugger.db"

    class config:
        env_file=".env"
        
settings=Settings()




