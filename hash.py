# @fichier main.py
# @titre 8 puzzle
# @description Resolve 8 puzzle game with heuristics and breadth_first_search
# @auteur Kevin Estalella
# @date 5 November 2016
# @version 1.0


hash_list = dict()

# Hash the state
def hash_state(node, state_size):
    hash = 0
    for i in range(0, state_size):
        hash += int(node.state[i] * pow(state_size, i))

    return hash