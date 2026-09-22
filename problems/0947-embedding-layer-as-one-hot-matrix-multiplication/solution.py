import numpy as np

def embedding_via_one_hot(token_ids, W):
    """
    Compute token embeddings via one-hot encoding and matrix multiplication.

    Args:
        token_ids: list or 1D array of integer token IDs
        W: numpy array of shape (vocab_size, embed_dim)

    Returns:
        numpy array of shape (len(token_ids), embed_dim)
    """
    
    # construct H 
    num_tokens = len(token_ids)
    vocab_size = len(W)

    H = np.zeros((num_tokens, vocab_size))

    for i in range(len(H)):
        j = token_ids[i]
        H[i][j] = 1

    return H @ W