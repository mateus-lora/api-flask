import sqlite3

class DataRepository:
    def __init__(self, db_path='data.db'):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    value TEXT NOT NULL
                )
            ''')

    def insert(self, value: str) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO data (value) VALUES (?)', (value,))
            conn.commit()

    def get_all(self) -> list:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, value FROM data')
            return cursor.fetchall() 