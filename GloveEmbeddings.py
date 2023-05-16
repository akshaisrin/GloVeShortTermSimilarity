import numpy as np

def load_glove_embeddings(path):
    """
    Load GloVe embeddings from a file.
    """
    embeddings_index = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
    return embeddings_index

def text_similarity(text1, text2, embeddings):
    """
    Calculate cosine similarity between the embeddings of two texts.
    """
    # tokenize the texts
    tokens1 = text1.lower().split()
    tokens2 = text2.lower().split()

    # calculate the embeddings of the tokens
    embeddings1 = np.array([embeddings.get(token, np.zeros(300)) for token in tokens1])
    embeddings2 = np.array([embeddings.get(token, np.zeros(300)) for token in tokens2])

    # calculate the cosine similarity between the two sets of embeddings
    similarity = np.dot(embeddings1.mean(axis=0), embeddings2.mean(axis=0)) / \
                 (np.linalg.norm(embeddings1.mean(axis=0)) * np.linalg.norm(embeddings2.mean(axis=0)))
    return similarity

# load GloVe embeddings
embeddings = load_glove_embeddings("C:\\Users\\aksha\\Downloads\\glove.42B.300d\\glove.42B.300d.txt")

# example usage
text1 = "The quick brown fox jumps over the lazy dog"
text2 = "A fast brown dog jumps over a lazy fox"
similarity = text_similarity(text1, text2, embeddings)
print("Similarity between the two texts:", similarity)
