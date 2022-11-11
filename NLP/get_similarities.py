from sentence_transformers import CrossEncoder
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import sqlalchemy as sa
import numpy as np
import pandas as pd
import json


# from text_processing import text_processing

def get_similarities_using_bi_encoder(df_text, df_id):
    # https://towardsdatascience.com/semantic-textual-similarity-83b3ca4a840e

    # Load the pre-trained model
    model = SentenceTransformer('stsb-mpnet-base-v2')
    # Generate Embeddings
    sentence_emb = model.encode(df_text, show_progress_bar=True)
    ids = df_id.to_numpy()
    np.save("NLP/embeddings", sentence_emb)
    np.save("NLP/ids", ids)

    engine = sa.create_engine('postgresql://django@openeduc-db:deploy-impact-2022@openeduc-db.postgres.database.azure.com:5432/openeduc-db', connect_args={"sslmode": "require"})
    df_embeddings = pd.DataFrame(columns=['embeding', 'edumaterial_id'])
    for i in range(len(ids)):
        json_file = json.dumps(sentence_emb[i,:].tolist())
        # json_file = json.dumps(sentence_emb[i,:].tolist()).encode()
        df_new_row = pd.DataFrame.from_dict([{'embeding': json_file, "edumaterial_id": df_id['id'].iloc[i]}])
        df_embeddings = pd.concat([df_embeddings,df_new_row], axis=0, ignore_index=True)
    df_embeddings.index.name = 'id'
    df_embeddings.to_sql('edu_data_embeddings', con=engine, if_exists='replace')

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
    tv_matrix = tv.fit_transform(df_text)
    tv_matrix = tv_matrix.toarray()

    vocab = tv.get_feature_names_out()
    # print(pd.DataFrame(np.round(tv_matrix, 2), columns=vocab))

    similarities = cosine_similarity(tv_matrix)

    return similarities

