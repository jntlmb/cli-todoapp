class Todo:

    def __init__(self, description, is_complete= False) -> None:
        self.description = description
        self.is_complete = is_complete

    def show_todos(self):
        for key, value in self.todo_dict:
            print(f"Todo: {key} / Status: {value}")