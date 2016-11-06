# -*- coding: utf-8 -*-

# @fichier main.py
# @titre 8 puzzle
# @description Resolve 8 puzzle game with heuristics and breadth_first_search
# @auteur Kevin Estalella
# @date 5 November 2016
# @version 1.0

from __future__ import print_function # to perform print without space

class Node(object):

    def __init__(self, state, prev_node=None):
        self.state = state
        self.prev = prev_node
        self.step = 0

