import sqlite3, hashlib
# to handle user registration and login using sqlite
class AuthDB:
    def __init__(self, db_path = 'library.db'):
        self.db_path = db_path
        self.create_table()

    # create user table if not exists

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLR IF NOT EXISTS user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT UNIQUE,
                email TEXT,
                password TEXT           )
        """)

        conn.commit()
        conn.close()