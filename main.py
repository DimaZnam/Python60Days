# user_prompt = "Type add or Show: "
""" """
todos = []

while True:

    user_action = input("Type add, show, exit: ").capitalize()
    match user_action:
        case "Add":
            todo  = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case  'Show':
            #print (todos)
            for item in todos:
                print("Bisness #: " , item)
        case 'Exit':
            break
        case whaterver
print ("----!!!!!____Done----!!!!!____")












z
    #   todos.append(todo.capitalize())

