# chatbot.py
import openai
import numpy as np
from config import OPENAI_API_KEY, LLM_MODEL
from embeddings import get_embedding

openai.api_key = OPENAI_API_KEY

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_most_relevant(query_embedding, embeddings, top_k=3):
    similarities = [cosine_similarity(query_embedding, np.array(item['embedding'])) for item in embeddings]
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    return [embeddings[i]['content'] for i in top_indices]

def generate_response(query, context):
    messages = [
        {"role": "system", "content": "You are a helpful assistant specializing in the aluminum industry. You will be provided with recent news articles as context. Your task is to answer user questions to the best of your ability using the information from the provided articles. If you are unable to find a direct answer in the articles, try to provide relevant information or insights based on what you do know.  Do not state that you do not have the information; instead, focus on extracting what is relevant from the provided context."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
    ]
    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=messages,
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def chat(query, embeddings):
    query_embedding = get_embedding(query)
    relevant_contexts = find_most_relevant(query_embedding, embeddings)
    context = " ".join(relevant_contexts)
    return generate_response(query, context)
