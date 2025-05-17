import sqlite3

def conectar(db_name):
    return sqlite3.connect(db_name)

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                tel TEXT NOT NULL,
                price REAL NOT NULL,
                date TEXT NOT NULL,
                cep TEXT NOT NULL
            );
        """)
    connection.commit()

def insert_client(connection, name, tel, price, date, cep):
    cursor = connection.cursor()
    cursor.execute("""
            INSERT INTO clients (name, tel, price, date, cep)
            VALUES (?, ?, ?, ?, ?)
        """, (name, tel, price, date, cep))

    connection.commit()