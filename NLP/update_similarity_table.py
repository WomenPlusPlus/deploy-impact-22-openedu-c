from pickle import TRUE
from plot_similarties import plot_similarities
import sqlalchemy as sa
import pandas as pd
import numpy as np
from pre_process_text import pre_process_text
import get_similarities as gs
import json
import datetime
# import os
# os.environ["TOKENIZERS_PARALLELISM"] = "false"

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
    
    COMPUTE_SIMILARITIES = True
    PREPROCESS = True
    METHOD = "BI_ENCODER" # choose between BI_ENCODER, CROSS_ENCODER and TF_IDF

    LOAD_SIMILARITIES = False
    LOAD_FROM_NEW_DB = True

    SAVE_SIMILARITIES = True

    UPDATE_DATABASE = True #this will overwrite the related project table in the new database

    PLOT = False

    if COMPUTE_SIMILARITIES == False and UPDATE_DATABASE == True:
        print("ERROR: We can not update the database because we don't have the ids of the projects")
        exit()


    if COMPUTE_SIMILARITIES == LOAD_SIMILARITIES:
        print("ERROR: either compute or load similarities.")
        exit()

    # query the text information of all projects
    if LOAD_FROM_NEW_DB:
        engine = sa.create_engine(
            'postgresql://django@openeduc-db:deploy-impact-2022@openeduc-db.postgres.database.azure.com:5432/openeduc-db', connect_args={"sslmode": "require"})
        df = pd.read_sql_query('SELECT title, description FROM edu_data_edumaterial', engine)
        df_text = df.apply(' '.join, axis=1)
        df_id_sito = pd.read_sql_query('SELECT id FROM edu_data_edumaterial', con=engine)
        #print(df_id_sito)


    else:
        engine = sa.create_engine('postgresql://deploy_impact:AVNS_tEdPMnvmmI0knrjJe-R@deploy-impact-cg-chrisg-demo.aivencloud.com:24947/openedu')
        df = pd.read_sql_query('SELECT title_en, subtitle_en, short_description_en FROM sito_project', engine) 
        df_text = df.apply(' '.join, axis=1)
        df_id_sito = pd.read_sql_query('SELECT id FROM sito_project', con=engine)
        #print(df_id_sito)


    n = len(df_text)

    if COMPUTE_SIMILARITIES:
        if PREPROCESS: 
            print("pre-processing-text...")
            for i in range(n):
                df_text.iloc[i] = pre_process_text(df_text.iloc[i], METHOD)


        # compare each text with eachother for similarities and store the value in the table
        similarities = np.zeros((n, n))
        print("computing similarities using method " + METHOD + "...")


        if METHOD == "BI_ENCODER":
            similarities = gs.get_similarities_using_bi_encoder(df_text)
        
        elif METHOD == "CROSS_ENCODER":
            "You chose the CROSS_ENCODER. This will take a while. Be patient!"
            similarities = gs.get_similarities_using_cross_encoder(df_text)

        elif METHOD == "TF_IDF":
            similarities = gs.get_similarities_using_tf_idf(df_text)

        else: 
            print("ERROR: Method isn't specified correctly.")
            print(METHOD)
            exit()
    
    if LOAD_SIMILARITIES:
        print("loading file: similarities.json")
        f = open("similarities.json")
        similarities = np.asarray(json.load(f))
        print(similarities)

    if SAVE_SIMILARITIES:
        print("saving similarity matrix in similarities.json")
        json_string = json.dumps(np.ndarray.tolist(similarities))
        file = open("similarities.json", "w")
        file.write(json_string)
        file.close()
        print("done")
    

    if PLOT:
        print("creating the plot...")
        plot_similarities(similarities, df_1["title_en"])
    
    if UPDATE_DATABASE:
        print("updating database...")

        n_related = 3

        engine = sa.create_engine('postgresql://django@openeduc-db:deploy-impact-2022@openeduc-db.postgres.database.azure.com:5432/openeduc-db', connect_args={"sslmode": "require"})

        df_related = pd.read_sql_query('SELECT * FROM edu_data_relatedprojects', con=engine)
        df_related.drop('id', axis=1, inplace=True)

        #engine_old = sa.create_engine('postgresql://deploy_impact:AVNS_tEdPMnvmmI0knrjJe-R@deploy-impact-cg-chrisg-demo.aivencloud.com:24947/openedu')



        for i in range(n):
            list_to_sort = np.zeros((n, 2))
            list_to_sort[:,0] = df_id_sito.id.values
            list_to_sort[:,1] = similarities[:,i]
            list_to_sort[i,1] = 0 #setting from 1 to 0 because we want to exclude the project itself
            sorted_list = list_to_sort[list_to_sort[:, 1].argsort()]
            #print(list_to_sort)
            #print(sorted_list)
            related = sorted_list[n:n-n_related-1:-1,0].astype(int)
            print("project " + str(i) + ": " + str(related))
            json_string = json.dumps(np.ndarray.tolist(related))


            #df_related.loc[:,['similarity', 'edumaterial_id']] = [json_string, i]
            df_related = df_related.append({'similarity': json_string, "edumaterial_id": df_id_sito['id'].iloc[i], "date" : datetime.datetime.now()}, ignore_index=True)

        df_related.index.name = 'id'
        df_related.to_sql('edu_data_relatedprojects', con=engine, if_exists='replace')


update_similarity_table()