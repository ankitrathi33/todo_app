FILEPATH = "todo.txt"

def get_todos(filepath= FILEPATH):
    """get the todo item from the text 
    file to a list.
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args,filepath= FILEPATH):
    """write the todo item to the 
    text file.
    """
    with open('todo.txt','w') as file:
        file.writelines(todos_args)
        
if __name__ == "__main__":
    print("Hello")
    print(get_todos())