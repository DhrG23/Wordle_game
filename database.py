import sqlite3

DB_NAME = 'wordle.db'

def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create words table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL UNIQUE
        )
    ''')

    # Insert some example words
    words = ["apple", "train", "stone", "plane", "smart"]
    cursor.executemany("INSERT OR IGNORE INTO words (word) VALUES (?)", [(word,) for word in words])

    conn.commit()
    conn.close()


def get_random_word():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT word FROM words ORDER BY RANDOM() LIMIT 1")
    word = cursor.fetchone()[0]

    conn.close()
    return word

print('done!!')
