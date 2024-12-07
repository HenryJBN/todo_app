import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Enter A Todo:")
input_box = fsg.InputText(tooltip="Enter a to-do", key='todo')
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todos(),
                       key='todos', enable_events=True, size=[45,10])
edit_button = fsg.Button("Edit")
window = fsg.Window("My To-do App",
                    layout=[[label], [input_box, add_button],[list_box, edit_button]],
                    font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
   # print(3, values['todos'][0])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']+'\n'
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WINDOW_CLOSED:
            break



window.close()