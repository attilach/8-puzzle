# @fichier main.py
# @titre 8 puzzle
# @description Resolve 8 puzzle game with heuristics and breadth_first_search
# @auteur Kevin Estalella
# @date 5 November 2016
# @version 1.0

from heapq import heappush, heappop


def heapsort(iterable):
    """sort the heap in argument

    Sort a heap structure ascending

    Args:
        iterable: The heapq of state visited yet

    Returns:
        The sorted heapq passed in argument
    """

    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]