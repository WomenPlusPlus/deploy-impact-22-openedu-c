from sentence_transformers import CrossEncoder
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd


# from text_processing import text_processing

def search_key_bi_encoder(df_text, search_key):
    # https://towardsdatascience.com/semantic-textual-similarity-83b3ca4a840e

    # Load the pre-trained model
    model = SentenceTransformer('stsb-mpnet-base-v2')

    # Generate Embeddings

    sentence_emb1 = model.encode(df_text, show_progress_bar=True)
    print('sentence_emb1', sentence_emb1)

    print(sentence_emb1.shape)

    sentence_emb2 = model.encode(search_key, show_progress_bar=True)
    sentence_emb2 = sentence_emb2.reshape(1, -1)
    print('sentence_emb2', sentence_emb2)
    print(sentence_emb2.shape)

    # Cosine Similarity
    similarity_score = cosine_similarity(sentence_emb1, sentence_emb2)

    return similarity_score