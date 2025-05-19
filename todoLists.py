import functions
while True:
  user_action = input("please type 'add' , 'show' , 'help' , 'edit' , 'delete' , 'complete' or 'exit' for actions ")
  user_action = user_action.strip()
  user_action = user_action.lower()

  
  if user_action.startswith("add") or user_action.startswith("new"):
    todo = user_action[4:] + '\n'

    todos = functions.get_todos()

    todos.append(todo)

    functions.give_todos(todos)

  elif user_action.startswith("show"):
    print("Here are your items: ")

    todos = functions.get_todos()

    for index , items in enumerate(todos):
      items = items.strip('\n')
      print(f"{index + 1}.{items}")
    print(f"you have {len(todos)} items in your list")  

  elif user_action.startswith("delete"):
    try:  
      user_delete = int(user_action[7:])
      user_delete -= 1

      todos = functions.get_todos()

      todos.pop(user_delete)

      functions.give_todos(todos)

      print("Your item  has been deleted, here are your other items: ")
      for index , items in enumerate(todos):
        items = items.strip("\n")
        print(f"{index + 1}.{items}")

    except ValueError:
      print("somthing wnet wrong lol , (only type number after edit)")   
      continue 
        
    except IndexError :
      print(" your number do not exist")
      continue  

  elif user_action.startswith("edit"):
    try:  
      edit_number = int(user_action[5:])
      edit_number -= 1

      todos = functions.get_todos()

      print(f"your item is {todos[edit_number]}")
      
      new_item = input("please edit your item: ") + "\n"
      todos[edit_number] = new_item

      functions.give_todos(todos)

    except ValueError:
      print("somthing wnet wrong lol , (only type number after edit)")   
      continue 

    except IndexError :
      print(" your number do not exist")
      continue

#    case "complete" | "Complete":
#      user_complete = int(input("please select the number of item which is complete: "))
#      user_complete -= 1
#
#      file = open('todos.txt' , 'r')
#      todos = file.readlines()
#      file.close()
#
#      todos[user_complete] = todos[user_complete] + "(Completed) \n"
#      for index , items in enumerate(todos):
#        print(f"{index + 1}.{items}")
#
#      file = open('todos' , 'w')
#      file.writelines(todos)
#      file.close()  

  elif user_action.startswith("help"):
    print("use 'add' for adding items to your todo list \n use 'edit' to edit a todo item \n use 'show' to show your todo list\n use 'delete' to delete an item in your todo list\n use 'complete' to complete your item todo list \n use 'exit' to exit the program.")

  elif user_action.startswith("exit"):
    break
  
  else:
    print("Unknown command, please try again")