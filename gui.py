import functions
import time
import FreeSimpleGUI as fsg
import os



if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

fsg.theme("darkGreen")
clock = fsg.Text('', key='clock')
label = fsg.Text("Enter A Todo:", size=10, )
input_box = fsg.InputText(tooltip="Enter a to-do", key='todo')
add_button = fsg.Button(image_source="add.png", tooltip="Add todo", key="Add")
list_box = fsg.Listbox(values=functions.get_todos(),
                       key='todos', enable_events=True, size=[45,10])
edit_button = fsg.Button("Edit")
complete_button =fsg.Button(image_source="complete.png",  tooltip="Complete Todo" , key='complete')
exit_button = fsg.Button("Exit")
# output = fsg.Text(key='output', text_color="red")
window = fsg.Window("My To-do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d %Y" "%H:%M:%S"))

    # print(2, values)
   # print(3, values['todos'][0])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window["todo"].update(value="")
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']+'\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
               fsg.popup("Please select an item first", font=("Helvetica", 20))
        case 'complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                fsg.popup("Select an item to complete", font=("Helvetica", 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case fsg.WINDOW_CLOSED:
            break



window.close()