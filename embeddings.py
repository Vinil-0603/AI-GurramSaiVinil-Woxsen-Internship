# embeddings.py
import openai
import numpy as np
from config import OPENAI_API_KEY, EMBEDDING_MODEL

openai.api_key = OPENAI_API_KEY

def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return response['data'][0]['embedding']

def create_embeddings(articles):
    embeddings = []
    for article in articles:
        text = f"{article['title']} {article['description']}"
        embedding = get_embedding(text)
        embeddings.append({
            'content': text,
            'embedding': embedding,
            'date': article['date']
        })
    return embeddings

# Export both functions
__all__ = ['get_embedding', 'create_embeddings']