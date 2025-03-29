from functions import get_todos, write_todos 
import time   

now = time.strftime("%b %d %Y %H:%M:%S")
print ("It is "+now)

while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    # To remove the spaces from user input we can use method str.trip(), it return the new string.
    user_action = user_action.strip()


   
    if 'add' in user_action:
        todo=user_action[4:]

        #Below method is made sure that file is close
        #Using Context Manager to optimize the code
        todo_list = get_todos()

        todo_list.append(todo + '\n')
        write_todos(todo_list)

    elif 'show' in user_action:

        todo_list = get_todos()

        #remove backslash characters with list compresion

        new_todo = [item.strip('\n') for item in todo_list]


        for index, item in enumerate(new_todo):
            item = item.title()
            print(f"{index+1}:{item}")

    elif 'edit' in user_action:
        try:
            number = user_action[5:]
            number = int(number)-1



            todo_list = get_todos()
            print(todo_list)

            update_todo = input(todo_list[number].strip('\n') + ":")
            todo_list[number] = update_todo + '\n'

            write_todos(todo_list)

            print("Todo List is Updated")
            
        except ValueError:
            print("Your command is not valid.")
            continue

    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])

            todo_list = get_todos()

            index = number-1
            todo_to_remove = todo_list[index].strip('\n')
            todo_list.pop(index)


            write_todos(todo_list)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")


print("Bye..")