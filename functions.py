FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns a list
    of to-do items
    """
    # using With Context Manager
    with open(filepath, "r") as _file:
        _todos = _file.readlines()
    return _todos


def write_todos(_todos, filepath=FILEPATH):
    """writes to-do list to a text file"""
    with open(filepath, 'w') as _file:
        _file.writelines(_todos)

# this ensures that codes below do not get executed
# when imported into a different program or file

print(__name__)
if __name__ == "__main__":
    print( "Hello from functions")