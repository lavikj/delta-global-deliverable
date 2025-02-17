"""
architecture.py

This file lays out the various object types and logic involved with ingestion.
"""


import os
from abc import ABC, abstractmethod, ABCMeta
from typing import List
import numpy
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


# Structure for each chunk
class Chunk:
    content: str

    def __init__(self, content: str):
        self.content = content


# Abstract class for documents
class Document(ABC):
    dir: str
    chunks: List[Chunk]
    embedder: SentenceTransformer

    @abstractmethod
    def load_chunks(self) -> None:
        """Load the chunks."""
        pass

    def __init__(self, dir: str, embedder: SentenceTransformer):
        self.dir = dir
        self.chunks = []
        self.embedder = embedder
        self.load_chunks()

    def get_embeddings(self) -> numpy.ndarray:
        return self.embedder.encode([chunk.content for chunk in self.chunks])
        

# Structure for each dataset
class Dataset:
    dir: str
    doctype: ABCMeta
    docs: List[Document]
    embedder: SentenceTransformer

    # Populate docs list with the appropriate document type
    def load_docs(self) -> None:
        print(f"Loading documents from {self.dir}")
        for file in tqdm(os.listdir(self.dir)):
            file = os.path.join(self.dir, file)
            self.docs.append(self.doctype(file, self.embedder))

    def __init__(self, dir: str, doctype: ABCMeta, embedder: SentenceTransformer):
        self.dir = dir
        self.doctype = doctype
        self.docs = []
        self.embedder = embedder
        self.load_docs()

    # Get the embeddings for each document
    def get_embeddings(self) -> List[numpy.ndarray]:
        embeddings = []
        print(f"Getting embeddings for {len(self.docs)} documents")
        for doc in tqdm(self.docs):
            embeddings.append(doc.get_embeddings())
        print()
        return embeddings
