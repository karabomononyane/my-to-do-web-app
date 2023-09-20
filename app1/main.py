#todos = []

while True:
    # Get user input and strip space chars
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            '''
            file = open("files/todos.txt", 'r')
            todos = file.readlines()
            file.close()
            '''

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            '''
            file = open("files/todos.txt", 'w')
            #file.writelines()
            file.writelines(todos)
            file.close()
            '''
            with open("files/todos.txt", 'w') as file:
                 todos = file.writelines(todos)

        case 'show'| 'display':
            '''
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            '''
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()


            new_todos = []
            '''
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            '''
            #List Comprehension
            #new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.title()
                item = item.strip('\n')
                #index = index -1
                row = f"{index+1}-{item}"
                print(row)
                #print(index, item)
        case 'edit':
            number = int(input("Number of the todo edit: "))
            number = number -1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'


            with open("files/todos.txt", 'w') as file:
                 todos = file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number-1)

            with open("files/todos.txt", 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list!"
            print(message)

        case 'exit':
            break

print("Bye!")







