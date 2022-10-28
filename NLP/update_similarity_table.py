from pickle import TRUE
import sqlalchemy as sa
import pandas as pd
import numpy as np
from pre_process_text import pre_process_text
import get_similarities as gs

# psycopg2


def update_similarity_table():
    """
    three different methods are implemented:
    BI_ENCODER: using SBERT model (https://www.sbert.net/docs/usage/semantic_textual_similarity.html)
    CROSS_ENCODER: using SBERT model 
    TF_IDF (https://drive.google.com/file/d/1OlJ7unCNCNAqNWSjQWlYDc3lXasjL_gn/view) we use a 
    vectorization containing the term frequency and the inverse term frequency looking at the
    entire text corpus
    """
    
    PREPROCESS = TRUE
    METHOD = "CROSS_ENCODER" # choose between BI_ENCODER, CROSS_ENCODER and TF_IDF

    # query the text information of all projects
    engine = sa.create_engine('postgresql://deploy_impact:AVNS_tEdPMnvmmI0knrjJe-R@deploy-impact-cg-chrisg-demo.aivencloud.com:24947/openedu')
    df_1 = pd.read_sql_query('SELECT title_en FROM sito_project', engine)
    df_2 = pd.read_sql_query('SELECT subtitle_en FROM sito_project', engine)
    df_3 = pd.read_sql_query('SELECT short_description_en FROM sito_project', engine) #TODO: remove css format
    df_4 = pd.read_sql_query('SELECT more_information_en FROM sito_project', engine) #TODO: remove css format
    df_combined = pd.concat([df_1, df_2, df_3], axis=1, join='inner')
    df_text = df_combined.apply(' '.join, axis=1)

    n = len(df_text)

    if PREPROCESS: 
        for i in range(n):
            df_text.iloc[i] = pre_process_text(df_text.iloc[i])


    # compare each text with eachother for similarities and store the value in the table
    similarities = np.zeros((n, n))

    if METHOD == "BI_ENCODER":
        similarities = gs.get_similarities_using_bi_encoder(df_text)
    
    elif METHOD == "CROSS_ENCODER":
        similarities = gs.get_similarities_using_cross_encoder(df_text)

    elif METHOD == "TF_IDF":
        similarities = gs.get_similarties_using_tf_idf(df_text)
    
    print(similarities)
    
    # update the table in the database


update_similarity_table()