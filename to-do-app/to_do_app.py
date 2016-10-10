import re

def print_lines(lines):
    print("You saved the following to-do items:")
    for i in range(len(lines)):
        print("\t" + str(i + 1) + ". " + lines[i], end="")

def read_database_lines():
    database = open("database.txt", "a+")
    database.seek(0, 0)
    lines = database.readlines()
    database.close()
    return lines

def write_database_lines(lines):
    database = open("database.txt", "w+")
    database.writelines(lines)
    database.close()    

def is_number(text):
    pattern = re.compile("^-?[0-9]+$")
    return pattern.match(text)

def list_items():
    lines = read_database_lines()
    print_lines(lines) 

def add():
    item = input("Add an item: ")
    lines = read_database_lines()
    lines.append("[ ] " + item + "\n")
    write_database_lines(lines)
    print("Item added.")
    
def mark():
    lines = read_database_lines()
    print_lines(lines)   
    comleted_item_index = input("Which one you want to mark as completed: ")
    if is_number(comleted_item_index):
        comleted_item_index = int(comleted_item_index)
        if comleted_item_index <= len(lines):
            lines[comleted_item_index - 1] = lines[comleted_item_index - 1][:1] + "x" + lines[comleted_item_index - 1][2:]
            print(lines[comleted_item_index - 1][3:-1] + " is completed")  
            write_database_lines(lines)

def archive():
    all_lines = read_database_lines()

    kept_lines = []
    for line in all_lines:
        if line[1] != 'x':
            kept_lines.append(line)

    write_database_lines(kept_lines)
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