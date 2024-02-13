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

    @staticmethod
    def list_todos():
        connection = sqlite3.connect('C:/Users/Jonathan/Projekte/Python/todoapp/database/todoapp')
        cursor = connection.cursor()
        
        cursor.execute('''SELECT * FROM todos''')
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]} / Status: {row[2]}")

        connection.close()

    @staticmethod
    def change_todo_status(todo_id):
        connection = sqlite3.connect('C:/Users/Jonathan/Projekte/Python/todoapp/database/todoapp')
        cursor = connection.cursor()
        
        cursor.execute('''SELECT status FROM todos WHERE id = ?''', (int(todo_id),))
        row = cursor.fetchone()

        #gpt
        if row is None:
            print(f"Todo with ID {todo_id} not found.")
            connection.close()
            return
    
        current_status = int(row[0])
        new_status = 1 - current_status

        try:     
            cursor.execute('''UPDATE todos SET status = ? WHERE id = ?''', (new_status, todo_id))
            connection.commit()
            print(f"Todo wiht ID {todo_id} status updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating status of todo with ID {todo_id}: {e}")

        connection.close()

        