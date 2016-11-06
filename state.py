# @fichier main.py
# @titre 8 puzzle
# @description Resolve 8 puzzle game with heuristics and breadth_first_search
# @auteur Kevin Estalella
# @date 5 November 2016
# @version 1.0

from list import *

def set_size():
    while True:
        size = int(input('Choose a state size [8, 15]: '))
        size += 1

        if sqrt(size).is_integer():
            return size
        else:
            print("Choose a valid size state")

def set_state(state_size):
    while True:
        state_generation_method = int(input('Tape 1 to generate random state number or 2 to select numbers: '))

        if state_generation_method == 1:
            state = generate_integer_list_random_between(0, state_size)
            return state
        elif state_generation_method == 2:
            state = generate_integer_list_between(0, state_size)
            return state