import faiss
import pickle
import numpy as np
from embed import embed_chunks

def load_index():
    index = faiss.read_index("faiss_index.idx")
    with open("chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def retrieve_top_k(query, k=3):
    index, chunks = load_index()
    query_vector = embed_chunks([query])[0]
    D, I = index.search(np.array([query_vector]).astype("float32"), k)
    return [chunks[i] for i in I[0]]
