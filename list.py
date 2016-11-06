# @fichier main.py
# @titre 8 puzzle
# @description Resolve 8 puzzle game with heuristics and breadth_first_search
# @auteur Kevin Estalella
# @date 5 November 2016
# @version 1.0

from __future__ import print_function # to perform print without space

from math import sqrt, pow
import random

# Generate a list with number of our choice
def generate_integer_list_between(min, max):

    state_list_items = range(min, max)

    state = []

    while len(state) < max-min:

        available_numbers = list(set(state_list_items) - set(state))  # do a diff
        print("Number availible: " + str(available_numbers))

        selected_number = input('Choose a number: ' + ': ')

        if selected_number not in state:
            state.append(selected_number)
        else:
            print("")

    return state


# Generate a list with random number
def generate_integer_list_random_between(min, max):
    list = []

    while len(list) < max:
        random_number = random.randrange(min, max)

        if random_number not in list:
            list.append(random_number)

    return list


# Print the list like a grid
def print_list_like_grid(list):
    list_size = len(list)

    i = 0
    string = ""
    nb_line = sqrt(list_size)  # nb char to print for each row

    while i < list_size:

        if i % nb_line == 0 and i != 0:
            print("")  # print a newline

        print(" " + str(list[i]), end='')

        i += 1

    print(string)

# Hash a list
def get_hash_list_indice(list_to_hash):
    list_size = len(list_to_hash)

    hash = 0
    for i in range(0, list_size):
        hash += int(list_to_hash[i] * pow(list_size, i))

    return hash