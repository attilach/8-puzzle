# @fichier main.py
# @titre 8 puzzle
# @description Resolve 8 puzzle game with heuristics and breadth_first_search
# @auteur Kevin Estalella
# @date 5 November 2016
# @version 1.0

from heapq import heappush, heappop
from math import sqrt
from sort import heapsort

# max iteration before stop searching
MAX_ITERATION = 1000000

def set_algo():
    """Choose an algorithm to resolve the puzzle

    Args:

    Returns:
        the response in integer format
    """

    while True:
        print('1) Simple breath_first_search - 2) hamming_search - 3) manhattan search')
        choice = int(input('Choose an algorithm to resolve this puzzle: '))

        if choice in [1,2,3]:
            return choice
        else:
            print("Choose a valid choice")


def breath_first_search(puzzle):
    """Breadth first search method to browse puzzle

    Browse the puzzle with breadth first search method and without strategy (blindly).

    Args:
        puzzle: An instance of object puzzle

    Returns:
        The response in list format. Return None if there is no solution (not in same space).
    """

    # Check if puzzle is solution
    if puzzle.node_start == puzzle.node_goal:
        return puzzle

    current_successors = puzzle.get_successors(puzzle.node_start)
    puzzle.nodes_stack.extend(current_successors)

    puzzle.node_start.prev = None

    while True:

        if puzzle.nodes_stack:
            current_node = puzzle.nodes_stack.popleft()
        else:
            return None

        if current_node.state == puzzle.node_goal.state or len(puzzle.nodes_stack) > MAX_ITERATION:
            return current_node
        else:
            current_successors = puzzle.get_successors(current_node)
            puzzle.nodes_stack.extend(current_successors)


def hamming_search(puzzle):
    """Bread first search method to browse puzzle with hamming

    Browse the puzzle with breadth first search method and with hamming strategy.

    Args:
        puzzle: An instance of object puzzle

    Returns:
        The response in list format. Return None if there is no solution (not in same space).
    """

    # Check if puzzle is solution
    if puzzle.node_start == puzzle.node_goal:
        return puzzle

    successors = puzzle.get_successors(puzzle.node_start)

    for item in successors:
        indice = hamming(item.state, puzzle.node_goal.state, puzzle.size)
        heappush(puzzle.heap, (indice, item))

    puzzle.node_start.prev = None

    while True:

        if puzzle.heap:
            current_node = heappop(puzzle.heap)
        else:
            return None

        if current_node[1].state == puzzle.node_goal.state or len(puzzle.heap) > MAX_ITERATION: #1'000'000
            return current_node
        else:
            successors = puzzle.get_successors(current_node[1])
            for item in successors:
                indice = hamming(item.state, puzzle.node_goal.state, puzzle.size)
                heappush(puzzle.heap, (indice, item))

            heapsorted = heapsort(puzzle.heap)
            puzzle.heap = heapsorted


def manhattan_search(puzzle):
    """Bread first search method to browse puzzle with manhattan

    Browse the puzzle with breadth first search method and with manhattan strategy.

    Args:
        puzzle: An instance of object puzzle

    Returns:
        The response in list format. Return None if there is no solution (not in same space).
    """

    # Check if puzzle is solution
    if puzzle.node_start == puzzle.node_goal:
        return puzzle

    successors = puzzle.get_successors(puzzle.node_start)

    for item in successors:
        indice = manhattan(item.state, puzzle.node_goal.state, puzzle.size)
        heappush(puzzle.heap, (indice, item))

    puzzle.node_start.prev = None

    while True:
        print(puzzle.cost)

        if puzzle.heap:
            current_node = heappop(puzzle.heap)
        else:
            return None

        if current_node[1].state == puzzle.node_goal.state or len(puzzle.heap) > MAX_ITERATION: #1'000'000
            return current_node
        else:
            successors = puzzle.get_successors(current_node[1])
            for item in successors:
                indice = manhattan(item.state, puzzle.node_goal.state, puzzle.size)
                heappush(puzzle.heap, (indice, item))

            heapsorted = heapsort(puzzle.heap)
            puzzle.heap = heapsorted


def hamming(new_state, state_goal, size):
    """Get hamming indice

    Args:
        new_state: A state to count misplaced number
        state_goal: The solution state
        size: The size of puzzle state

    Returns:
        The response in integer correspond to misplaced case
    """

    count = 0
    for i in new_state:
        if new_state[i] == state_goal[i]:
            count += 1

    return size - count


def manhattan(new_state, state_goal, size):
    """Get manhattan indice for a state

    Get the sum of distance who separate each case to is solution

    Args:
        new_state: A state to count misplaced number
        state_goal: The solution state
        size: The size of puzzle state

    Returns:
        The response in integer correspond to sum of distance who separate each case to is solution
    """

    sizesqrt = sqrt(size)
    count = 0
    for item in state_goal:
        num_row_current_item = new_state.index(item) // sizesqrt  # Get num row current item
        num_row_goal_item = state_goal.index(item) // sizesqrt  # Get num row goal item

        num_col_current_item = int(new_state.index(item) % sizesqrt)  # Get num col current item
        num_col_goal_item = int(state_goal.index(item) % sizesqrt)  # Get num col goal item

        row_result = abs(num_row_current_item - num_row_goal_item)
        col_result = abs(num_col_current_item - num_col_goal_item)

        result = row_result + col_result

        count += result

    return count