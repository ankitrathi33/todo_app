import function_todoapp
import time

now = time.strftime("%d %b %Y %H:%M:%S")
print("it is:", now)

while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()
    
    
    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = function_todoapp.get_todos()
        
        todos.append(todo + '\n')
        
        function_todoapp.write_todos(todos)
        
    elif user_action.startswith("show"):
        
        todos = function_todoapp.get_todos()
        
        for index,item in enumerate(todos):
            item = item.strip()
            print(f"{index+1}-{item}")
            
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = function_todoapp.get_todos()
                
            new_todo = input("Ener new todo:")
            todos[number] = new_todo +"\n"
            
            function_todoapp.write_todos(todos)
            
        except ValueError:
            print("Your command is invalid,try again")
            continue
        
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = function_todoapp.get_todos()
            
            index = number-1
            todo_to_remove = todos[index]
            todos.pop(index)
            
            function_todoapp.write_todos(todos)
                
            message = f"todo{todo_to_remove} had been completed."
            print(message)
        except IndexError:
            print("Your index is out of bound.")
            continue
        
    elif user_action.startswith("exit"):
        break 
    
    else:
        print('Action is not defined.')
        
print("bye!")

