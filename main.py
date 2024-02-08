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
    todo_dict[new_todo.description] = new_todo.is_complete 

def show_todos():
    counter = 1
    for todo, is_complete in todo_dict.items():
        if is_complete == False:
            print(f"{counter}. Todo: {todo} / Status: Not Complete")
            counter += 1
        else:
            print(f"{counter}. Todo: {todo} / Status: Complete")
            counter += 1

def complete_todo():
    show_todos()
    operation = user_input("Enter Index of the Todo to change the Status from: ")

    counter = 1
    for key in todo_dict.keys():
        if counter == int(operation):
            key_to_change = key
        counter += 1
        
    if key_to_change in todo_dict:
        if todo_dict[key_to_change] == False:
            todo_dict[key_to_change] = True
        else:
            todo_dict[key_to_change] = False
    
        

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
            delete_todo()
        else:
            continue     
    else:
        quit()