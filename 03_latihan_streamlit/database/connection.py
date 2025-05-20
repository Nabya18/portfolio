import streamlit as st
import bcrypt
import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="latihan",
        user="user",
        password="root",
        port=5432
    )

def check_login(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE email = %s", (email,))
    result = cur.fetchone()
    cur.close()
    conn.close()

    if result:
        hashed_password = result[0]
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
    else:
        return False