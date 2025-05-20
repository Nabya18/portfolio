import bcrypt
import psycopg
from .connection import get_connection

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")

def insert_user(name, email, password):
    conn = get_connection()
    cur = conn.cursor()

    hashed_password = hash_password(password)

    cur.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, hashed_password)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_total_users():
    conn = psycopg.connect(
        host="localhost",
        dbname="latihan",
        user="user",
        password="root",
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    total = cur.fetchone()[0]
    cur.close()
    conn.close()
    return total