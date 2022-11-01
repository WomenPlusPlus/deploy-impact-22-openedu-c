import sqlalchemy as sa
import pandas as pd
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()


# for using postgres one also needs to install psycopg2
engine = sa.create_engine(os.getenv("DB_OPENEDU")) #?sslmode=preferred')
engine_new = sa.create_engine(os.getenv("DB_OPENEDU_NEW"),
                              connect_args={"sslmode": "require"})

df_new = df = pd.read_sql_query('SELECT * FROM edu_data_edumaterial',
                       con=engine_new)



df = pd.read_sql_query('SELECT * FROM sito_project ',
                       con=engine)

for id, row in df.iterrows():
    #print(BeautifulSoup(row.more_information_en).get_text().replace('\n',''))
    #row.title_en
    #'id', 'title', 'description', 'reviewed', 'id_Institution_id','id_Media_Channel_id', 'id_author_id', 'id_publisher_id'
    df_new = df_new.append(
        {'id': id,
         'title': row.title_en,
         'description': row.subtitle_en +
                        row.srow.short_description_en.replace('\xa0', ' ') +
                        BeautifulSoup(row.more_information_en, "html.parser").get_text().replace('\n', ''),
         'reviewed': row.published
         }, ignore_index=True)

df_new.to_sql('edu_data_edumaterial', con=engine_new, index_label='id', index=False, if_exists='append')


# df = pd.read_sql_query('SELECT * FROM sito_project '
#                        'INNER JOIN sito_contenttype ON sito_project.content_type_id=sito_contenttype.id',
#                        con=engine)


