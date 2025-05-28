import os

# Update these values with your PostgreSQL credentials
DB_USER = 'postgres'
DB_PASSWORD = 'adaaja'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'finalitdp'

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"