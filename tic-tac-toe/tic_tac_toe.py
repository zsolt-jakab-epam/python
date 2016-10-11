import os

clear = lambda: os.system('cls')
empy_cell = "_"
hum_cell = "X"
comp_cell = "O"


def is_winner(table):
    if table[0:3].count(hum_cell) == 3:
        return True
    if table[3:6].count(hum_cell) == 3:
        return True    
    if table[6:9].count(hum_cell) == 3:
        return True    
    if table[0] == hum_cell and table[3] == hum_cell and table[6] == hum_cell:
        return True                 
    if table[1] == hum_cell and table[4] == hum_cell and table[7] == hum_cell:
        return True      
    if table[2] == hum_cell and table[5] == hum_cell and table[8] == hum_cell:
        return True                 
    if table[0] == hum_cell and table[4] == hum_cell and table[8] == hum_cell:
        return True     
    if table[2] == hum_cell and table[4] == hum_cell and table[6] == hum_cell:
        return True     
    if table[0:3].count(comp_cell) == 3:
        return True
    if table[3:6].count(comp_cell) == 3:
        return True    
    if table[6:9].count(comp_cell) == 3:
        return True    
    if table[0] == comp_cell and table[3] == comp_cell and table[6] == comp_cell:
        return True                 
    if table[1] == comp_cell and table[4] == comp_cell and table[7] == comp_cell:
        return True      
    if table[2] == comp_cell and table[5] == comp_cell and table[8] == comp_cell:
        return True                 
    if table[0] == comp_cell and table[4] == comp_cell and table[8] == comp_cell:
        return True     
    if table[2] == comp_cell and table[4] == comp_cell and table[6] == comp_cell:
        return True   
    return False

def calculate_comp_index(table):
    return table.index(empy_cell)

def print_table(table):
    clear()
    for i in range(3):
        my = table[(i * 3) : (i * 3 + 3)]
        print(''.join(my))

table = [empy_cell for i in range(9)]

print_table(table)

while True:
    hum_index = int(input()) - 1
    table[hum_index] = hum_cell
    print_table(table)
    if is_winner(table):
        print("There is a Winner!")
        break
    com_index = calculate_comp_index(table)
    table[com_index] = comp_cell
    print_table(table)
    if is_winner(table):
        print("There is a Winner!")
        break
    

    
