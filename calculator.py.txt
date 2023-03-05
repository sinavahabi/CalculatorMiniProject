"""
    Program: Calculator
    Author: sina vahabi
    Copyright: 2023/01
"""

import re


print("Welcome")
print("Type '0' to exit the program.\n")

previous, run = 0, True


def do_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input('Enter your equation: ')
    else:
        equation = input(str(previous))
    if equation == '0':
        run = False
        print('Goodbye.')
    else:
        equation = re.sub(r'[^\d.+*-/()]', '', equation)
    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)


while run:
    do_math()
