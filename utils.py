import json

def save_embeddings(embeddings, filename='embeddings.json'):
    with open(filename, 'w') as f:
        json.dump(embeddings, f)

def load_embeddings(filename='embeddings.json'):
    with open(filename, 'r') as f:
        return json.load(f)