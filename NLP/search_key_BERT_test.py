
from pickle import TRUE
from plot_similarties import plot_similarities
import sqlalchemy as sa
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

search_key = 'Science Competition'

engine = sa.create_engine('postgresql://deploy_impact:AVNS_tEdPMnvmmI0knrjJe-R@deploy-impact-cg-chrisg-demo.aivencloud.com:24947/openedu')
df = pd.read_sql_query('SELECT title_en, subtitle_en, short_description_en FROM sito_project', engine)
df_1 = pd.read_sql_query('SELECT title_en FROM sito_project', engine)
df_text = df.apply(' '.join, axis=1)

print(df_text)


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

print(similarity_score, df_1)

#  OK!!! It returns the similarity_score based on the search key in the correct way!!!

# TODO: We've to implement a threshold of similarity to decide automatically how many project have to be seen