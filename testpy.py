## consine_similarity test
import numpy as np
from scipy.sparse import csr_matrix
from scipy.spatial.distance import cosine

def compute_cosine_similarity(sparse_matrix1, sparse_matrix2):
    # Ensure that both input matrices are in Compressed Sparse Row (CSR) format
    if not isinstance(sparse_matrix1, csr_matrix) or not isinstance(sparse_matrix2, csr_matrix):
        raise ValueError("Input matrices must be in CSR format")

    # Convert the sparse matrices to dense arrays
    dense_matrix1 = sparse_matrix1.toarray()
    dense_matrix2 = sparse_matrix2.toarray()

    # Compute the cosine similarity between the dense arrays
    similarity = 1 - cosine(dense_matrix1, dense_matrix2)

    return similarity
