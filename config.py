import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SCRAPE_URL = "https://news.metal.com/list/industry/aluminium"
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-4"  