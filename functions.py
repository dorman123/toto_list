def get_todos(file_path="todos.txt"):
    """
    Read from todos.txt and return the list
    of all the todo items.

    :param file_path: str
    :return: list
    """
    with open(file_path, 'r') as file:
        return file.readlines()


def write_todos(todos_arg, file_path="todos.txt"):
    """
    Gets a list of all the todos tasks and
    write them to the todos.txt file.

    :param todos_arg: list
    :param file_path: str
    :return: None
    """
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)
