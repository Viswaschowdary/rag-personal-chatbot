import faiss
import numpy as np
import pickle
from dotenv import load_dotenv
load_dotenv()


def build_faiss_index(vectors, dim):
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))
    return index

def save_index(index, vectors, chunks):
    faiss.write_index(index, "faiss_index.idx")
    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
