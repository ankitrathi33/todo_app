import function_todoapp
import PySimpleGUI as psg
import time

psg.theme("Black")

clock = psg.Text('',key='clock')
label = psg.Text("Type in a todo:")

input_box = psg.InputText(tooltip="Enter a Todo",
                          key="todo")

add_buttton = psg.Button(size=2,image_source="add.png",
                         mouseover_colors="LightBlue2",
                         tooltip="Add_item",
                         key = 'Add')

list_box = psg.Listbox(values = function_todoapp.get_todos(),
                       key ='todos',
                       enable_events = True, 
                       size = [45,10])

edit_button = psg.Button("Edit")

complete_button = psg.Button(size=2,image_source="complete.png",
                             mouseover_colors="LightBlue2",
                             tooltip="Complete_item",
                             key="Complete")
exit_button = psg.Button("Exit")

window = psg.Window("Todo-App",
                    layout = [[clock],
                              [label],
                              [input_box,add_buttton],
                              [list_box,edit_button,complete_button],
                              [exit_button]],
                    font = ('Helvitica',20))

while True:
    event, values = window.read(timeout = 10)
    window['clock'].update(value = time.strftime("%d %b %Y %H:%M:%S"))
    print(1,values)
    print(2,event)
    print(3,values['todos'])
    
    match event:
        case'Add':
            todos = function_todoapp.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function_todoapp.write_todos(todos)
            window['todos'].update(values = todos)
            
        case'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                
                todos = function_todoapp.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function_todoapp.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                psg.popup("Please select a value first.",font=('Helvitica',20))
                
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function_todoapp.get_todos()
                todos.remove(todo_to_complete)
                function_todoapp.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = "")
            except IndexError:
                psg.popup("Please select a value first.",font=('Helvitica',20))
            
        case "Exit":
            break 
        
        case 'todos':
            window['todo'].update(value = values['todos'][0])
            
        case psg.WIN_CLOSED:
            break

window.close()

