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

    # helper function hash password simple and safe

    def hash_password(self, password):
        """"Hashing password using SHA256"""
        return hashlib.sha3_256(password.encode()).hexdigest()
    
    # Register new user

    def register_user(self, username, email,password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        hashed = self.hash_password(password)

        try:
            cursor.execute(
                "INSERT INTO user (username, email, password) VALUES(?, ?, ?)",
                (username, email, hashed)
            )
            conn.commit()
            conn.close()
            return True #'Registaration successfull'
        except sqlite3.IntegrityError:
            conn.close()
            return False # user already exists
        
    # validate login

    def validate_login(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        hashed = self.hash_password(password)
        cursor.execute(
            "SELECT * FROM user WHERE username = ? AND password = ?",
            (username, password)
            )
        user = cursor.fetchone()
        conn.close()

        if user:
            return True # Login successful
        return False # Incorrect username            
