import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Enter A Todo:")
input_box = fsg.InputText(tooltip="Enter a to-do", expand_y=300)
add_button = fsg.Button("Add")
window = fsg.Window("My To-do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()