import sqlite3

class Database:
    def __init__(self, db_path="duo_tcg.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_tables(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                capability TEXT,
                descriptor TEXT,
                distinction TEXT,
                energy INTEGER,
                attack INTEGER,
                life INTEGER,
                description TEXT,
                card_type TEXT
            )
            
        """)

    def save_character(self, card):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO characters (
                    name,
                    capability,
                    descriptor,
                    distinction,
                    energy,
                    attack,
                    life,
                    description,
                    card_type
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                card.name,
                card.capability,
                card.descriptor,
                card.distinction,
                card.energy,
                card.attack,
                card.life,
                card.description,
                card.card_type
            ))


    def get_characters(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM characters")
            return cursor.fetchall()