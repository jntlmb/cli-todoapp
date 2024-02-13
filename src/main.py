from todo import Todo

todo_dict = {}

def print_menu():
    print("""
1) Create Todo
2) Show Todo
3) Complete Todo
4) Delete Todo
Q) Quit
""")

def user_input(message):
    return input(message)

def create_todo(description):
    new_todo = Todo(description, False)
    new_todo.save_to_db() 

def show_todos():
    Todo.list_todos()

def complete_todo():
    show_todos()
    todo_id = user_input("Enter ID of Todo you like to change the Status from: ")
    Todo.change_todo_status(todo_id)

#update
def delete_todo():
    show_todos()
    operation = user_input("Enter Index of the Todo to delete: ")

    counter = 1
    for key in todo_dict.keys():
        if counter == int(operation):
            key_to_delete = key
        counter += 1

    if key_to_delete in todo_dict:
        del todo_dict[key_to_delete]


    

while True:
    print_menu()
    operation = user_input("Enter Operation: ")
    if operation.isdigit():
        if int(operation) == 1:
            todo_description = user_input("Enter Todo: ")
            create_todo(todo_description)
        elif int(operation) == 2:
            show_todos()
        elif int(operation) == 3:
            complete_todo()
        elif int(operation) == 4:
            pass
        else:
            continue     
    else:
        quit()