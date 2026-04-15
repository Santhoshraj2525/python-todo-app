FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Return the list of To-dos from the todos.txt file."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)