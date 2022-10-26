import sqlalchemy as sa
import pandas as pd
import numpy as np
# psycopg2

def check_similarity(text_1, text_2):
    if text_1 == text_2:
        return 1
    else:
        return 0.1

def update_similarity_table():
    # query the text information of all projects
    engine = sa.create_engine('postgresql://deploy_impact:AVNS_tEdPMnvmmI0knrjJe-R@deploy-impact-cg-chrisg-demo.aivencloud.com:24947/openedu')
    df_1 = pd.read_sql_query('SELECT title_en FROM sito_project', engine)
    df_2 = pd.read_sql_query('SELECT subtitle_en FROM sito_project', engine)
    df_3 = pd.read_sql_query('SELECT short_description_en FROM sito_project', engine) #TODO: remove css format
    df_4 = pd.read_sql_query('SELECT more_information_en FROM sito_project', engine) #TODO: remove css format
    df_combined = pd.concat([df_1, df_2, df_3, df_4], axis=1, join='inner')
    df_text = df_combined.apply(' '.join, axis=1)  

    # compare each text with eachother for similarities and store the value in the table
    n = len(df_text)
    similarities = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            similarities[i,j] = check_similarity(df_text.iloc[i], df_text.iloc[j])
    print(similarities)
    
    # update the table in the database


update_similarity_table()