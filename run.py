'''
run.py

This file executes the ingestion pipeline.
The user needs to specify only the directory and the implemented class name.
Optionally, the user can specify the embedding model. By default, the embedding
model is set to 'sentence-transformers/all-MiniLM-L6-v2'.
'''


from typing import List
import numpy
import pickle
from Ingestion.DocumentTypes import FinanceDocument, FootballDocument
from Ingestion.Architecture import Dataset
from sentence_transformers import SentenceTransformer


def get_embeddings(classes: dict, embedder = SentenceTransformer(
        'sentence-transformers/all-MiniLM-L6-v2')) -> List[List[numpy.ndarray]]:

    # Traverse through the given directories, create Datasets out of them, and 
    # acquire the embeddings for each
    embeddings = []
    for dir, cls in classes.items():
        dataset = Dataset(dir, cls, embedder)
        embeddings.append(dataset.get_embeddings())
    return embeddings


if __name__ == "__main__":
    
    # User specifies the directory and the implemented class name
    datasets = {
        "data/football": FootballDocument,
        "data/finance": FinanceDocument
    }

    # Request embeddings for the specified datasets
    embeddings = get_embeddings(datasets)

    # Save the embeddings to a file
    with open("embeddings.pkl", "wb") as f:
        pickle.dump(embeddings, f)

    print("Embeddings saved to embeddings.pkl!")
    
