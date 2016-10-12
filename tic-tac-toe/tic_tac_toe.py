import os
import re

empy_cell = " "
hum_cell = "X"
comp_cell = "O"

def clear(): 
    os.system('cls')

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

def no_more_step(table):
    return table.count(empy_cell) == 0

def calculate_comp_index(table):
    return table.index(empy_cell)

def is_last_cell_in_row(cell_ind):
    return cell_ind  == 2 or cell_ind  == 5 or cell_ind  == 8

def print_cell(cell_ind, cell):
    if is_last_cell_in_row(cell_ind):
        print(cell, end='\n')
    else:
        print(cell + '|', end='')

def print_table(table):
    clear()
    for cell_ind, cell in enumerate(table):
        print_cell(cell_ind, cell)
        if is_last_cell_in_row(cell_ind):
            print('-----')

def is_game_ended(table):
    return is_winner(table) or no_more_step(table)

def input_human_index(table):
    input_pattern = re.compile("^[1-9]$")
    while True:
        hum_input = str(input())
        if input_pattern.match(hum_input):
            hum_index = int(hum_input) - 1
            if table[hum_index] == empy_cell:
                return hum_index 

def hum_step(table):
    while True:
        print_table(table)
        hum_index = input_human_index(table)
        if table[hum_index] == empy_cell:
            break
    table[hum_index] = hum_cell
    print_table(table)


def comp_step(table):
    print_table(table)
    com_index = calculate_comp_index(table)
    table[com_index] = comp_cell
    print_table(table)

def print_result(table):
    if is_winner(table):
        print("There is a winner!")
    else:
        print("The game is ended with a tie!")

def main():
    table = [empy_cell for i in range(9)]

    while True:
        hum_step(table)
        if is_game_ended(table):
            break
        comp_step(table)
        if is_game_ended(table):
            break

    print_result(table)

main()