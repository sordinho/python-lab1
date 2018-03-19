# To Do manager

def printMenu():
    print("------------------------------------------")
    print("1) Insert a new task")
    print("2) Remove a task")
    print("3) Show tasks")
    print("4) Exit")
    print("Inserire la scelta ---> ")

printMenu()
cmd = input()
n = 0
tasks = list()
while cmd != '4':
    printMenu()
    if cmd == '1':
        task = input()
        tasks.append[task]
    elif cmd == '2':
        target = input()
        tasks.remove(target)
    elif cmd == '3':
        print(tasks)
