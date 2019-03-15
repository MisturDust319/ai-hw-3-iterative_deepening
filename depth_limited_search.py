"""
Pseudocode (from AIMA textbook)

function DEPTH-LIMITED-SEARCH(problem, l) returns a solution, or failure, or cutoff
 frontier ← a FIFO queue initially containing one path, for the problem's initial state
 solution ← failure
 while frontier is not empty do
   parent ← pop(frontier)
   if depth(parent) > l then
     solution ← cutoff
   else
     for child in successors(parent) do
       if child is a goal then
         return child
       add child to frontier
 return solution
"""

from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        # either derive depth from parent, or start at 1
        if parent:
            self.depth = parent.depth+1
        else:
            self.depth = 1

    def compare(self, other):
        return self.state == other.state

    def print_path(self):
        """
        print the path of the solution to the problem
        """
        # print the parent's data before this data
        if self.parent:
            self.parent.print_path()
        # print this node's data
        self.print_data()

    def print_data(self):
        """
        instructions on how to print this node's data
        """
        print("Depth: " + str(self.depth) + " State: " + str(self.state))

    def solution(self):
        """
        Contains instructions on how to act when a solution is found
        By default, it prints the path
        """
        self.print_path()


class Problem:
    def __init__(self, start, end, actions):
        """
        Class that represents a problem, including it's starting point, the goal,
        and instructions on how to reach the goal
        :param start:
        The starting state of the problem
        :param end:
        The end goal state of the problem
        :param actions:
        A callback that calculates solutions to the problem
            :param state:
                the current state of a problem used to calculate possible next
                steps for the problem
        """
        self.start = start
        self.end = end
        self.actions = actions



def depth_limited_search(problem, cutoff):
    """
    Searches for a solution to problem
    :param problem:
    :param cutoff:
    :return:
    """
    def recursive_dls(node, limit):
        # check if solution was found
        if node.compare(problem.end):
            return node.solution()
        elif limit == 0:
            # return cutoff if at depth limit
            return problem.cutoff()
        else:
            # otherwise, start the recursive search process
            cutoff_occured = False
            # compute a possible action
            for action in problem.actions(node.state):
                # create a child node
                # using the resulting action as state
                child = Node(action, node)
                # recursively search with the new child node as a start point
                result = recursive_dls(child, limit-1)

                # end early if a cutoff occured
                if result == cutoff:
                    cutoff_occured = True
                elif result is not None:
                    return result
            if cutoff_occured:
                # end early if cutoff occurred
                return cutoff

