import psycopg

from psycopg.rows import dict_row

conn_params = {
       'host': 'localhost',
       'port': 5433,
       'dbname': 'apsecApp',
       'user': 'postgres',
       'password': 'postgres'
   }

conn = psycopg.connect(**conn_params, row_factory=dict_row)