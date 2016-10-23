import os
import re

def clear(): 
    os.system('cls')

def check_indicies_type(table, indicies, cell_type):
    for i in indicies:
        if table[i] != cell_type:
            return False
    return True

def is_win_situ(table, cell_type):
    for line in lines:
        if check_indicies_type(table, line, cell_type):
            return True
    return False

def is_winner(table): 
    return is_win_situ(table, hum_cell) or is_win_situ(table, comp_cell)

def no_more_step(table):
    return table.count(empty_cell) == 0

def count_indicies_type(table, indicies, cell_type):
    counter = 0
    for i in indicies:
        if table[i] == cell_type:
            counter += 1 
    return counter

def get_first_index(table, indicies, cell_type):
    for i in indicies:
        if table[i] == cell_type:
            return i
    return -1

def calc_def_index(table):
    for line in lines:
        if count_indicies_type(table, line, hum_cell) == 2 and count_indicies_type(table, line, empty_cell):
            return get_first_index(table, line, empty_cell)
    if table.count(empty_cell) == 8 and table.index(hum_cell) != middle_index:
        return middle_index            
    return -1

def calc_att_index(table):
    for line in lines:
        if count_indicies_type(table, line, comp_cell) == 2 and count_indicies_type(table, line, hum_cell) == 0:
            return get_first_index(table, line, empty_cell)
    for line in lines:
        if count_indicies_type(table, line, comp_cell) == 1 and count_indicies_type(table, line, hum_cell) == 0:
            return get_first_index(table, line, empty_cell) 
    for line in lines:
        if count_indicies_type(table, line, hum_cell) == 0:
            return get_first_index(table, line, empty_cell)              
    return -1    

def calc_win_index(table):
    for line in lines:
        if count_indicies_type(table, line, comp_cell) == 2 and count_indicies_type(table, line, hum_cell) == 0:
            return get_first_index(table, line, empty_cell)
    return -1

def calc_comp_index(table):
    comp_index = calc_win_index(table)
    if comp_index != -1: 
        return comp_index   
    comp_index = calc_def_index(table)
    if comp_index != -1:
        return comp_index
    comp_index = calc_att_index(table)
    if comp_index != -1:
        return comp_index
    return table.index(empty_cell)

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
        if is_last_cell_in_row(cell_ind) and cell_ind < 8:
            print('-----')

def is_game_ended(table):
    return is_winner(table) or no_more_step(table)

def input_human_index(table):
    while True:
        print_table(table)
        hum_input = str(input())
        if input_pattern.match(hum_input):
            return int(hum_input) - 1 

def hum_step(table):
    while True:
        hum_index = input_human_index(table)
        if table[hum_index] == empty_cell:
            break
    table[hum_index] = hum_cell
    print_table(table)


def comp_step(table):
    print_table(table)
    com_index = calc_comp_index(table)
    table[com_index] = comp_cell
    print_table(table)

def print_result(table):
    if is_winner(table):
        print('There is a winner!')
    else:
        print('The game is ended with a tie!')

def main():
    table = [empty_cell for i in range(number_of_cells)]
    while True:
        hum_step(table)
        if is_game_ended(table):
            break
        comp_step(table)
        if is_game_ended(table):
            break

    print_result(table)

input_pattern_text = '^[1-9]$'
input_pattern = re.compile(input_pattern_text)

empty_cell = ' '
hum_cell = 'X'
comp_cell = 'O'

middle_index = 4
number_of_cells = 9

first_line  = [0, 1, 2]
second_line = [3, 4, 5]
third_line  = [6, 7, 8]
first_row   = [0, 3, 6]
second_row  = [1, 4, 7]
third_row   = [2, 5, 8]
major_diag  = [0, 4, 8]
minor_diag  = [6, 4, 2]

lines = [major_diag, minor_diag, first_line, second_line, third_line, first_row, second_row, third_row]

main()