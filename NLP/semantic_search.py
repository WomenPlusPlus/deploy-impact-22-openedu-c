import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import sqlalchemy as sa
import json

"""
    Arguement: search_key - String with the word that the user wants to do the search
    Return argument: ids - a list of project id's that need will be displayed to user
"""


def semantic_search(search_key):
    # search_key = 'Science Competition'

    # threshold = 0.25
    # path_embeddings = "/home/claudia/Documents/women++/deploy-impact-22-openedu-c/NLP/embeddings.npy"
    # path_ids = "/home/claudia/Documents/women++/deploy-impact-22-openedu-c/NLP/ids.npy"

    # loading the embeddings and the ids from binary file
    ##project_embeddings = np.load(path_embeddings, allow_pickle=True)
    ##ids = np.load(path_ids, allow_pickle=True)

    engine = sa.create_engine(
        'postgresql://django@openeduc-db:deploy-impact-2022@openeduc-db.postgres.database.azure.com:5432/openeduc-db',
        connect_args={"sslmode": "require"})
    df_id = pd.read_sql_query('SELECT id, title FROM edu_data_edumaterial',
                              con=engine)  # without title the ids were sorted.
    ids = df_id.drop(['title'], axis=1).to_numpy()
    df_embeddings = pd.read_sql_query('SELECT embeding FROM edu_data_embeddings', con=engine)

    n = len(ids)
    project_embeddings = np.zeros((n, 768))

    for i in range(n):
        project_embeddings[i:] = json.loads(df_embeddings["embeding"].iloc[i])

    # Load the pre-trained model
    model = SentenceTransformer('stsb-mpnet-base-v2')

    # computing embedding of search_key
    search_key_embedding = model.encode(search_key, show_progress_bar=False)
    search_key_embedding = search_key_embedding.reshape(1, -1)

    # compute cosine similarity
    similarity_score = cosine_similarity(project_embeddings, search_key_embedding)

    # find ids where similarity score is larger than thresshold

    sim_score = np.append(similarity_score, ids, axis=1)
    # print(sim_score)

    df_sim_score = pd.DataFrame(sim_score, columns=['sim_score', 'id_project'])
    # print(df_sim_score)

    df1 = df_sim_score.sort_values(by="sim_score", ascending=False)
    related_project = df1.query('sim_score > 0.30')['id_project']

    return (related_project)