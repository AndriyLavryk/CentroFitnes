import sqlite3
import os

class Connection:
    DB_NAME = 'app.db'
    DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)

    @classmethod
    def get_connection(cls):
        # Devuelve una conexión SQLite
        return sqlite3.connect(cls.DB_PATH)

    @classmethod
    def release_connection(cls, connection):
        # Cierra la conexión SQLite
        connection.close()

    @classmethod
    def init_db(cls):
        # Crea la base de datos y la tabla `clients` si no existen
        connection = cls.get_connection()
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                membership INTEGER NOT NULL
            )
        ''')

        connection.commit()
        cls.release_connection(connection)
        print("Base de datos y tabla 'clients' inicializadas.")


if __name__ == '__main__':
    Connection.init_db()
    conn = Connection.get_connection()
    print("Conexión establecida:", conn)
    Connection.release_connection(conn)
