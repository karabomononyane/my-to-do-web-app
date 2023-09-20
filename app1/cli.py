#from functions import get_todos, write_todos

import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is: ", now)

text = """
Principles of productivity:
Managing you inlow.
Systemetizing everything that reports.
"""

while True:
    # Get user input and strip space chars
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:].title() + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        new_todos = []

        # List Comprehension
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            # index = index -1
            row = f"{index + 1}-{item}"
            print(row)
            # print(index, item)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list!"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid.")

print("Bye!")
