from sentence_transformers import CrossEncoder
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# from text_processing import text_processing

def get_similarities_using_bi_encoder(df_text):
    # https://towardsdatascience.com/semantic-textual-similarity-83b3ca4a840e

    # Load the pre-trained model
    model = SentenceTransformer('stsb-mpnet-base-v2')
    # Generate Embeddings
    sentence_emb = model.encode(df_text, show_progress_bar=True)

    # Cosine Similarity
    similarity_score = cosine_similarity(sentence_emb)

    return similarity_score

def get_similarities_using_cross_encoder(df_text):
    # https://towardsdatascience.com/semantic-textual-similarity-83b3ca4a840e
    model = CrossEncoder('cross-encoder/stsb-roberta-base')

    n = len(df_text)
    similarities = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            similarities[i][j] = model.predict([df_text.iloc[i], df_text.iloc[j]], show_progress_bar=True)

    return similarities

    
def get_similarities_using_tf_idf(df_text):
    # https://drive.google.com/file/d/1OlJ7unCNCNAqNWSjQWlYDc3lXasjL_gn/view)

    tv = TfidfVectorizer(min_df=0., max_df=1., norm='l2', use_idf=True)
    tv_matrix = tv.fit_transform(norm_corpus)
    tv_matrix = tv_matrix.toarray()

    vocab = tv.get_feature_names_out()
    pd.DataFrame(np.round(tv_matrix, 2), columns=vocab)
    # not done yet ...

    similarities = np.zeros((n, n))


    return similarity_score

