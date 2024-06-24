import os


def get_todos(todos_local):
    """ Read a text file and return a list of
        to-do items
    """
    filepath = os.path.join(os.getcwd(), "todos.txt")
    with open(filepath, "r") as file_local:
        todos_local =[line.strip() for line in file_local.readlines()]
    return todos_local


def write_todos(todos_args, filepath):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        todos = file.writelines(todos_args)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
