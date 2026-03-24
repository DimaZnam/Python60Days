while True:
    user_action = input("Type add, show, edit, def, complete, exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo  = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case  'show' | 'display':
            #print (todos)
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()



            print(todos)

            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            #print ("Got it!")
            number = int (input("Enter a number of the todo to edit: "))
            number = number-1
            buffer = todos [number]
            new_todo = input ("Enter New todo: ")
            todos [number] = new_todo
            print ("Old value: ",buffer, " New value: ", todos [number])
        case "def":
            todos = ["first", "second", "third"]
        case "complite":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break

        case _:
            print("Hey, you entered an unknow command")

print ("----!!!!!____Done----!!!!!____")

# 06 - Day 6 APP 1