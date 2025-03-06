 #!/bin/bash -x
set -e
echo "begining of tab"
psql --username "postgres" --dbname "appsec_db" --port 5432 <<-EOSQL
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    isAdmin BOOLEAN DEFAULT FALSE,
    password TEXT NOT NULL
);
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
);
EOSQL
echo "success"
