import sqlite3

class Todo:

    def __init__(self, description, is_complete= False) -> None:
        self.description = description
        self.is_complete = is_complete
        
    def save_to_db(self):
        connection = sqlite3.connect('C:/Users/Jonathan/Projekte/Python/todoapp/database/todoapp')
        cursor = connection.cursor()
        
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY,
                    task TEXT,
                    status TEXT
                    )
                    ''')
        
        cursor.execute('''INSERT INTO todos (task, status) VALUES (?, ?)''', (self.description, self.is_complete))
        connection.commit()
        connection.close()
        
        