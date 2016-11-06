# @fichier main.py
# @titre 8 puzzle
# @description Resolve 8 puzzle game with heuristics and breadth_first_search
# @auteur Kevin Estalella
# @date 5 November 2016
# @version 1.0

from collections import deque

from node import *
from state import *
from hash import *


class Puzzle(Node):

    def __init__(self):
        self.size = set_size()

        self.node_start = Node(set_state(self.size))
        self.node_goal = Node(set_state(self.size))

        self.nodes_stack = deque()
        self.heap = []
        self.cost = 0


    def move(self, current_node, successors, pos, steps):

        new_node = Node(list(current_node.state), current_node)

        # swap values
        new_node.state[pos] = current_node.state[pos + steps]
        new_node.state[pos + steps] = current_node.state[pos]

        print("node.goal")
        print(self.node_goal.state)
        print("new.state")
        print(new_node.state)

        if new_node != current_node.prev:
            hash = hash_state(new_node, self.size)

            try:
                hash_list[hash]
            except KeyError:
                hash_list[hash] = new_node
                new_node.prev = current_node
                new_node.step = current_node.step + 1
                successors.append(new_node)
                self.cost += 1



    # Get successors possibility of the state
    def get_successors(self, current_node):

        successors = []
        pos = current_node.state.index(0)
        width = int(sqrt(self.size))
        row = pos / width
        col = pos % width

        if row > 0:
            # move up
            self.move(current_node, successors, pos, -width)

        if col > 0:
            # move left
            self.move(current_node, successors, pos, -1)

        if row < width - 1:
            # move down
            self.move(current_node, successors, pos, width)

        if col < width - 1:
            # move right
            self.move(current_node, successors, pos, 1)

        return successors