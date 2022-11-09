import numpy as np  
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def semantic_search(search_key):
    """
    Arguement: search_key - String with the word that the user wants to do the search
    Return argument: ids - a list of project id's that need will be displayed to user
    """ 
    threshold = 0.25
    path_embeddings = "NLP/embeddings.npy"
    path_ids = "NLP/ids.npy"
    # loading the embeddings and the ids from binary file
    project_embeddings = np.load(path_embeddings, allow_pickle=True)
    ids = np.load(path_ids, allow_pickle=True)

    # Load the pre-trained model
    model = SentenceTransformer('stsb-mpnet-base-v2')

    # computing embedding of search_key
    search_key_embedding = model.encode(search_key, show_progress_bar=False)
    search_key_embedding = search_key_embedding.reshape(1, -1)


    # compute cosine similarity
    similarity_score = cosine_similarity(project_embeddings, search_key_embedding)

    # find ids where similarity score is larger than thresshold
    related_ids = ids where similarity_score > threshold

    return related_ids
