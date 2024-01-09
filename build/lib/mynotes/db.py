# mynotes/db.py
import json
import bcrypt
import psycopg2

def connect_to_database():
     return psycopg2.connect(
        host="tyke.db.elephantsql.com",
        user="gmrjgzau",
        password="5RwL-M8dRMefWDRjmCmn_0_KwSCB7BhP",
        database="gmrjgzau"
    )

def create_tables():
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE,
                password_hash TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                id SERIAL PRIMARY KEY,
                group_name TEXT UNIQUE,
                user_id INTEGER REFERENCES users(id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id SERIAL PRIMARY KEY,
                unique_id TEXT UNIQUE,
                timestamp TEXT,
                note_text TEXT,
                group_name TEXT,
                user_id INTEGER REFERENCES users(id)
            )
        """)
        conn.commit()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def create_user(username, password):
    create_tables()
    password_hash = hash_password(password)
    with connect_to_database() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, password_hash))
            conn.commit()
        except psycopg2.IntegrityError as e:
            print(f"Username already exists. Choose a different username. Error: {e}")
        except Exception as e:
            print(f"Error during user creation: {e}")

def authenticate_user(username, password):
    create_tables()
    with connect_to_database() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, password_hash FROM users WHERE username=%s", (username,))
            user_data = cursor.fetchone()
            if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data[1]):
                with open("temporaryDb.json", "w") as f:
                    json.dump({"session": user_data[0]}, f)
                return user_data[0]
            else:
                return None
        except Exception as e:
            return None

def syncData():
    print("not available")
