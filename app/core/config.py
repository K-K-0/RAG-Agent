from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    open_api_key: str = ""
    llm_model: str = "gpt-4o-mini"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    data_dir: str = "data"
    vector_store_dir: str = "vectore_store"
    chund_size: int = 500
    chunk_overlap: int = 50
    top_k: int = 3

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
