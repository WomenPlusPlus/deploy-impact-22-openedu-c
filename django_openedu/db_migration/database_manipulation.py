import sqlalchemy as sa
import pandas as pd
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
# for using postgres one also needs to install psycopg2

def migrate_projects(engine, engine_new):
    df_new = df = pd.read_sql_query('SELECT * FROM edu_data_edumaterial',
                           con=engine_new)

    df = pd.read_sql_query('SELECT * FROM sito_project ',
                           con=engine, index_col='id')

    for id, row in df.iterrows():
        #print(BeautifulSoup(row.more_information_en).get_text().replace('\n',''))
        #row.title_en
        #'id', 'title', 'description', 'reviewed', 'id_Institution_id','id_Media_Channel_id', 'id_author_id', 'id_publisher_id'
        df_new = df_new.append(
            {'id': id,
             'title': row.title_en,
             'description': row.subtitle_en + '. ' +
                            row.short_description_en.replace('\xa0', ' ') + '. ' +
                            BeautifulSoup(row.more_information_en, "html.parser").get_text().replace('\n', ''),
             'reviewed': row.published
             }, ignore_index=True)

    df_new.to_sql('edu_data_edumaterial', con=engine_new, index_label='id', index=False, if_exists='append')

def migrate_many_to_many(engine, engine_new):
    table_new = 'edu_data_level'
    table_cats = 'sito_level'
    table_new_join = 'edu_data_edumaterial_level'
    table_join = 'sito_project_level'
    df_new_cats = df = pd.read_sql_query(f'SELECT * FROM {table_new}',
                                         con=engine_new)

    df_cats = pd.read_sql_query(f'SELECT * FROM {table_cats} ',
                                con=engine, index_col='id')

    df_new_join = df = pd.read_sql_query(f'SELECT * FROM {table_new_join}',
                                         con=engine_new)

    df_join = pd.read_sql_query(f'SELECT * FROM {table_join} ',
                                con=engine, index_col='id')

    for id, row in df_cats.iterrows():
        #print(BeautifulSoup(row.more_information_en).get_text().replace('\n',''))
        #row.title_en
        #'id', 'title', 'description', 'reviewed', 'id_Institution_id','id_Media_Channel_id', 'id_author_id', 'id_publisher_id'
        df_new_cats = df_new_cats.append(
            {'id': id,
             'name': row.title_en},
            ignore_index=True)

    df_new_cats.to_sql(f'{table_new}', con=engine_new, index_label='id', index=False, if_exists='append')


# df = pd.read_sql_query('SELECT * FROM sito_project '
#                        'INNER JOIN sito_contenttype ON sito_project.content_type_id=sito_contenttype.id',
#                        con=engine)


if __name__ == '__main__':

    engine = sa.create_engine(os.getenv("DB_OPENEDU"))  # ?sslmode=preferred')
    engine_new = sa.create_engine(os.getenv("DB_OPENEDU_NEW"),
                                  connect_args={"sslmode": "require"})

    # migrate_projects(engine, engine_new)
