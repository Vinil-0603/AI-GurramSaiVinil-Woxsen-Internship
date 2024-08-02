import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
SCRAPE_URL = "https://news.metal.com/list/industry/aluminium"
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-4"  
