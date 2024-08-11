# DISPLAY
def display_operations():
     print("""
        Press 1 to ADD
        Press 2 to DELETE
        Press 3 to VIEW
        Press 4 to EXIT
        """)
     
# TASKS
tasks = [] 

# ADD TASKS
def add_task():
    task = input('\nEnter your task :')
    tasks.append(task)
    print('Your task "{}" is added sucessfully'.format(task))

# VIEW THE TASKS
def view_tasks():
    if not tasks:
        print('No tasks available')
    else:
         for i in range(len(tasks)):
              print(f'{i+1}. {tasks[i]}')

    # for i, tasks in enumerate(tasks, start=1):
    #      print(f'{i}. {tasks}')
         
# DELETE TASKS
def delete_tasks():
    if not tasks:
        print('No tasks available')
        return
    
    view_tasks()
    del_number = int(input('\nEnter the task number you want to delete :'))
    if del_number > len(tasks):
        print('Invalid task number')
    else:
        del tasks[del_number - 1]
        remove_task = tasks.pop(del_number - 1)
        print('{} deleted sucessfully'.format(remove_task))

    
# EXIT FROM LOOP
def exit_tasks():
      print('Thanks for using Time World')
      print('Exiting ...')

# MAIN LOOP
print('WELCOME TO TIME WORLD !')
while True:
    display_operations()
    choices = int(input('Enter the 1 to 4 :'))
    
    if choices == 1:
        add_task()
    elif choices == 2:
        delete_tasks()
    elif choices == 3:
        view_tasks()
    elif choices == 4:
        exit_tasks()
        break
    else:
        print('Choose vaild operation')
        

# TIME -> 09:34AM Sunday, 11 August 2024 