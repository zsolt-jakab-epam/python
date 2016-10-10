def print_lines(lines):
    print("You saved the following to-do items:")
    for i in range(len(lines)):
        print("\t" + str(i + 1) + ". " + lines[i], end="")

def read_database_lines():
    database = open("database.txt", "r")
    lines = database.readlines()
    database.close()
    return lines

def write_database_lines()
    database = open("database.txt", "w+")
    database.writelines(lines)
    database.close()    

def list_items():
    print_lines(read_database_lines())

def add():
    database = open("database.txt", "a")
    item = input("Add an item: ")
    database.write("[ ] " + item + "\n")
    print("Item added.")
    database.close()

def mark():
    lines = read_database_lines()
    print_lines(lines)
    
    comleted_item_index = int(input("Which one you want to mark as completed: "))
    
    if comleted_item_index <= len(lines):
        lines[comleted_item_index - 1] = lines[comleted_item_index - 1][:1] + "x" + lines[comleted_item_index - 1][2:]
        print(lines[comleted_item_index - 1][3:-1] + " is completed")  

    write_database_lines()

def archive():
    lines = read_database_lines():

    database = open("database.txt", "w+")
    for i in range(len(lines)):
        if lines[i][1] != 'x':
            database.write(lines[i])
    database.close()
    print("All completed tasks got deleted.")    

command = input("Please specify a command [list, add, mark, archive]: ")

if command == "list":
    list_items()

elif command == "add":
    add()

elif command == "mark":    
    mark()

elif command == "archive":      
    archive()