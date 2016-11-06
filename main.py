# -*- coding: utf-8 -*-

# @fichier main.py
# @titre 8 puzzle
# @description Resolve 8 puzzle game with heuristics and breadth_first_search
# @auteur Kevin Estalella
# @date 5 November 2016
# @version 1.0

from puzzle import *
from algorithm import *

# Main program

# Print welcome message
print("#######################################")
print("# Indication: 0 is the case empty     #")
print("#######################################\n")

puzzle = Puzzle()

# Show information
print("\nPuzzle start: ")
print(puzzle.node_start.state)

print("\nPuzzle goal: ")
print(puzzle.node_goal.state)


print("\nPuzzle start: ")
print_list_like_grid(puzzle.node_start.state)

print("\nPuzzle goal: ")
print_list_like_grid(puzzle.node_goal.state)


choice = 3

if choice == 1:
    result = breath_first_search(puzzle)
elif choice == 2:
    result = hamming_search(puzzle)
elif choice == 3:
    result = manhattan_search(puzzle)


if choice == 1:
    if result:
        print("\nResultat")
        print(result.state)
        print("STEP")
        print(result.step)
        print("COST")
        print(puzzle.cost)
    else:
        print("Both state are not in same space")

elif choice == 2 or choice == 3:
    if result:
        print("\nResultat")
        print(result[1].state)
        print("STEP")
        print(result[1].step)
        print("COST")
        print(puzzle.cost)
    else:
        print("Both state are not in same space")





# print("nbr successeurs")
# print(len(all_succ))