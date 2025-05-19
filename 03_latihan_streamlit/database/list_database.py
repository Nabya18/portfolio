import psycopg

def list_database():
    with psycopg.connect(
        host="localhost",
        dbname="latihan",
        user="user",
        password="root",
        port=5432
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT ")