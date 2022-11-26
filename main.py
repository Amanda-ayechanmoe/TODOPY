while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    # To remove the spaces from user input we can use method str.trip(), it return the new string.
    user_action = user_action.strip()


    match user_action:
        case 'add':
            todo=input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todo_list = file.readlines()
            file.close()

            todo_list.append(todo)

            file = open('todos.txt','w')
            file.writelines(todo_list)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todo_list = file.readlines()
            file.close()

            #remove backslash characters with for loop

            #new_todo = []

            #for item in todo_list:
                #new_todo.append(item.strip('\n'))

            #remove backslash characters with list compresion

            new_todo = [item.strip('\n') for item in todo_list]


            for index, item in enumerate(new_todo):
                item = item.title()
                print(f"{index+1}:{item}")

        case 'edit':
            number = input("Number of the todo to edit: ")
            idx = int(number)-1
            update_todo = input(todo_list[idx] + ":")
            todo_list[idx] = update_todo
            print("Todo List is Updated")

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            file = open('todos.txt', 'r')
            todo_list = file.readlines()
            file.close()

            todo_list.pop(number-1)

            file = open('todos.txt', 'w')
            file.writelines(todo_list)
            file.close()

        case 'exit':
            break
    #if none of the case is matched
        case _:
            print("Hey, you entered undefined comment")


print("Bye..")