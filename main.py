while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    # To remove the spaces from user input we can use method str.trip(), it return the new string.
    user_action = user_action.strip()


    match user_action:
        case 'add':
            todo=input("Enter a todo: ") + "\n"


            #file = open('todos.txt', 'r')
            #todo_list = file.readlines()
            #file.close()

            #Below method is made sure that file is close
            #Using Context Manager to optimize the code
            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            todo_list.append(todo)

            with open('todos.txt','w') as file:
                file.writelines(todo_list)

        case 'show':

            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

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



            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()
            print(todo_list)

            update_todo = input(todo_list[idx].strip('\n') + ":")
            todo_list[idx] = update_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)

            print("Todo List is Updated")

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            index = number-1
            todo_to_remove = todo_list[index].strip('\n')
            todo_list.pop(index)


            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
    #if none of the case is matched
        case _:
            print("Hey, you entered undefined comment")


print("Bye..")