import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="latihan",
        user="user",
        password="root",
        port=5432
    )