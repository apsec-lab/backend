import psycopg

from psycopg.rows import dict_row

from env import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD

conn_params = {
       'host': DB_HOST,
       'port': DB_PORT,
       'dbname': DB_NAME,
       'user': DB_USER,
       'password': DB_PASSWORD
   }

conn = psycopg.connect(**conn_params, row_factory=dict_row)