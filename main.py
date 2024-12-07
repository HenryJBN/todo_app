#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S""")
print(" It is ", now)
while True:
    prompt = input("Enter add, show , edit, complete or exit: ").strip()

    if prompt.startswith("add"):
        todo = prompt[4:] + "\n"

        # Call get_todos
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif prompt.startswith("show"):
        todos = functions.get_todos()
        # use List comprehension
        # new_todos =[ item.strip('\n') for item in todos]
        # or remove the new line on the fly within the loop
        for index, item in enumerate(todos):
            row =f"{index+1}-{item.strip('\n')}"
            print(row)

    elif prompt.startswith("edit"):
        try:
            number = int(prompt[5:])
            number = number -  1
            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo +'\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your entered an invalid command")
            continue

    elif prompt.startswith("complete"):
        try:
            number = int(prompt[9:])
            todos = functions.get_todos()
            index = number-1
            todo_to_remove = todos[index]
            todos.pop(index)
            functions.write_todos(todos)
            message =f"todo {todo_to_remove.strip('\n')} was removed from the list"
            print(message)
        except(IndexError, ValueError) as e:
            print("Your entered an invalid command")
            continue
    elif prompt.startswith("exit"):
        break
    else :
        print("Hey, you entered an unknown command")

print("Bye !!! ")





