import numpy as np
import pickle

with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)

print("Loaded a list of items:", len(data))
print("First item length:", len(data[0]))
print("Second item length:", len(data[1]))
print("First Document Embeddings:", data[0][0], np.shape(data[0][0]))
print("Random Document Embeddings:", data[1][3], np.shape(data[1][3]))