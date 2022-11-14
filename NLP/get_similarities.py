from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import sqlalchemy as sa
import numpy as np
import pandas as pd
import json

def get_similarities_using_bi_encoder(df_text, df_id):
    # https://towardsdatascience.com/semantic-textual-similarity-83b3ca4a840e

    # Load the pre-trained model
    model = SentenceTransformer('stsb-mpnet-base-v2')
    # Generate Embeddings
    sentence_emb = model.encode(df_text, show_progress_bar=True)
    ids = df_id.to_numpy()

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