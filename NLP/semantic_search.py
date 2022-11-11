import numpy as np  
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import sqlalchemy as sa
import pandas as pd
import json

def semantic_search(search_key):
    """
    Arguement: search_key - String with the word that the user wants to do the search
    Return argument: ids - a list of project id's that need will be displayed to user
    """ 
    threshold = 0.25

    LOADING_METHOD = "DATABASE" # NPY_FILES or DATABASE

    if LOADING_METHOD == "NPY_FILES": 
        # loading the embeddings and the ids from binary file
        path_embeddings = "NLP/embeddings.npy"
        path_ids = "NLP/ids.npy"
        project_embeddings = np.load(path_embeddings, allow_pickle=True)
        ids = np.load(path_ids, allow_pickle=True)

    elif LOADING_METHOD == "DATABASE":
        engine = sa.create_engine('postgresql://django@openeduc-db:deploy-impact-2022@openeduc-db.postgres.database.azure.com:5432/openeduc-db', connect_args={"sslmode": "require"})
        df_embeddings = pd.read_sql_query('SELECT * FROM edu_data_embeddings', con=engine) #without title the ids were sorted.
        ids = df_embeddings['edumaterial_id'].to_numpy().reshape((-1,1))

        data = json.loads(df_embeddings["embeding"].iloc[0])
        # iterate through the projects and convert json to numpy array of shape (32, 768)
        n = len(ids)
        project_embeddings = np.zeros((n, 768))
        for i in range(n):
            project_embeddings[i,:] = json.loads(df_embeddings["embeding"].iloc[i]) # jsonb file -> numpy array

    else:
        print("Cannot load embeddings. Choose a correct loading method.")
        exit()

    # Load the pre-trained model
    model = SentenceTransformer('stsb-mpnet-base-v2')

    # computing embedding of search_key
    search_key_embedding = model.encode(search_key, show_progress_bar=False)
    search_key_embedding = search_key_embedding.reshape(1, -1)

    # compute cosine similarity
    similarity_score = cosine_similarity(project_embeddings, search_key_embedding)

    # find ids where similarity score is larger than thresshold
    list_to_sort = np.concatenate((ids, similarity_score), axis=1)
    sorted_list = np.flip(list_to_sort[list_to_sort[:, 1].argsort()],axis=0)
    related_ids = sorted_list[sorted_list[:,1]>threshold,0].astype(int)

    return related_ids

search_keys_test = ["Science Competition", "language", "encyclopedia", "database", \
    "travel", "school", "medicine", "university", "research", "jungle", "kitchen", \
    "rain", "elephant", "grass", "cars", "sun", "children", "chair"]
for i in search_keys_test:
    print(i)
    print(semantic_search(i))