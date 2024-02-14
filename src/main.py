from todo import Todo


def print_menu():
    print("""
1) Create Todo
2) Change Todo Status
3) Delete Todo
Q) Quit
""")

def user_input(message):
    return input(message)

def create_todo(description):
    new_todo = Todo(description, False)
    new_todo.save_to_db() 

def change_status(todo_id):
    Todo.change_todo_status(todo_id)

def delete_todo(todo_id):
    Todo.delete_todo(todo_id)
    

while True:
    Todo.list_todos()
    print_menu()
    operation = user_input("Enter Operation: ")
    if operation.isdigit():
        if int(operation) == 1:
            todo_description = user_input("Enter Todo: ")
            create_todo(todo_description)
        elif int(operation) == 2:
            todo_id = user_input("Enter ID of Todo you like to change the Status from: ")
            change_status(todo_id)
        elif int(operation) == 3:
            todo_id = user_input("Enter Todo ID: ")
            delete_todo(todo_id)
        else:
            continue     
    else:
        quit()