from pickle import TRUE
import sqlalchemy as sa
import pandas as pd
import numpy as np
from pre_process_text import pre_process_text
from get_similarities import get_similarities_using_bi_encoder
import json
import datetime


def update_database():
    """
    This function must be called after a new project has been added to the database or the project title 
    or description has been modified.

    This function will load the text information from the database and recompute the three most similar projects
    using the SBERT model with the bi-encoder for a STS analysis. These related a project ids are then being added
    to the corresponding database table with a timestamp.

    In addition, the embedding vecotors calculated in the STS analysis are stored in the database. These are used 
    for fast semantic search queries on the websites.
    """
    
    # loading text description and ids form the database
    engine = sa.create_engine('postgresql://django@openeduc-db:deploy-impact-2022@openeduc-db.postgres.database.azure.com:5432/openeduc-db',\
         connect_args={"sslmode": "require"})
    df = pd.read_sql_query('SELECT title, description FROM edu_data_edumaterial', engine)
    df_text = df.apply(' '.join, axis=1)
    df_id = pd.read_sql_query('SELECT id, title FROM edu_data_edumaterial', con=engine) #without title the ids were sorted.
    df_id = df_id.drop(['title'], axis=1)

    n = len(df_text)
    
    print("pre-processing-text...")
    for i in range(n):
        df_text.iloc[i] = pre_process_text(df_text.iloc[i])

    # compare each text with eachother for similarities and store the value in a n by n matrix
    similarities = np.zeros((n, n))
    print("computing similarities using SBERT model with bi-encoder...")
    similarities = get_similarities_using_bi_encoder(df_text, df_id)
    
    print("updating the related projects in the database...")
    n_related = 3
    df_related = pd.read_sql_query('SELECT * FROM edu_data_relatedprojects', con=engine)
    df_related.drop('id', axis=1, inplace=True)

    # finding for every project the three most related projects
    for i in range(n):
        list_to_sort = np.zeros((n, 2))
        list_to_sort[:,0] = df_id.id.values
        list_to_sort[:,1] = similarities[:,i]
        list_to_sort[i,1] = 0 #setting from 1 to 0 because we want to exclude the project itself
        sorted_list = list_to_sort[list_to_sort[:, 1].argsort()]
        related = sorted_list[n:n-n_related-1:-1,0].astype(int)
        json_string = json.dumps(np.ndarray.tolist(related))
        df_new_row = pd.DataFrame.from_dict([{'similarity': json_string, "edumaterial_id": df_id['id'].iloc[i], "date" : datetime.datetime.now()}])
        df_related = pd.concat([df_related, df_new_row], axis=0, ignore_index=True)

    # updating the related projects in the database
    df_related.index.name = 'id'
    df_related.to_sql('edu_data_relatedprojects', con=engine, if_exists='replace')
    print("done")


update_database()