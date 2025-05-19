def get_todos(pathfile = 'todos.txt'):
  with open(pathfile , 'r') as file:
    todos_get = file.readlines()
  return todos_get

def give_todos(todos_arg , pathfile='todos.txt'):
  with open (pathfile , 'w') as file:
    file.writelines(todos_arg)

