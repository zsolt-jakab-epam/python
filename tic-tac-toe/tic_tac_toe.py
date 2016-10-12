import os
import re

def clear(): 
    os.system('cls')

def check_indicies_type(indicies, cell_type):
    for i in indicies:
        if table[i] != cell_type:
            return False
    return True

def is_win_situ(lines, cell_type):
    for line in lines:
        if check_indicies_type(line, cell_type):
            return True
    return False

def is_winner(): 
    lines = [first_line, second_line, third_line, first_row, second_row, third_row, major_diag, minor_diag]
    return is_win_situ(lines, hum_cell) or is_win_situ(lines, comp_cell)

def no_more_step():
    return table.count(empy_cell) == 0

def calculate_comp_index():
    return table.index(empy_cell)

def is_last_cell_in_row(cell_ind):
    return cell_ind  == 2 or cell_ind  == 5 or cell_ind  == 8

def print_cell(cell_ind, cell):
    if is_last_cell_in_row(cell_ind):
        print(cell, end='\n')
    else:
        print(cell + '|', end='')

def print_table():
    clear()
    for cell_ind, cell in enumerate(table):
        print_cell(cell_ind, cell)
        if is_last_cell_in_row(cell_ind):
            print('-----')

def is_game_ended():
    return is_winner() or no_more_step()

def input_human_index():
    input_pattern = re.compile("^[1-9]$")
    while True:
        print_table()
        hum_input = str(input())
        if input_pattern.match(hum_input):
            return int(hum_input) - 1 

def hum_step():
    while True:
        hum_index = input_human_index()
        if table[hum_index] == empy_cell:
            break
    table[hum_index] = hum_cell
    print_table()


def comp_step():
    print_table()
    com_index = calculate_comp_index()
    table[com_index] = comp_cell
    print_table()

def print_result():
    if is_winner():
        print("There is a winner!")
    else:
        print("The game is ended with a tie!")

def main():
    while True:
        hum_step()
        if is_game_ended():
            break
        comp_step()
        if is_game_ended():
            break

    print_result()

empy_cell = " "
hum_cell = "X"
comp_cell = "O"

first_line  = [0, 1, 2]
second_line = [3, 4, 5]
third_line  = [6, 7, 8]
first_row   = [0, 3, 6]
second_row  = [1, 4, 7]
third_row   = [2, 5, 8]
major_diag  = [0, 4, 8]
minor_diag  = [6, 4, 2]

table = [empy_cell for i in range(9)]

main()