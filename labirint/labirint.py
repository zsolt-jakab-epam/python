import os
import os

clear = lambda: os.system('cls')
clear()


def read_labirint():
    labirint_file = open(labirint_file_path, "r")
    lines = labirint_file.readlines()
    labirint_file.close()
    return lines

def print_lines(lines):
    for line in lines:
        print(line, end="")    

dir = os.path.dirname(os.path.abspath(__file__))

labirint_file_path = os.path.join(dir, 'labirint.txt')

labirint = read_labirint()

while True:
    a = input()
    clear()
    print_lines(labirint)
    if a == "a":
        break
