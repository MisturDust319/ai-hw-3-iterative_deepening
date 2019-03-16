from depth_limited_search import *

def iterative_deepening_search(problem):
    """
    Performs a depth limited search at a regularly increasing depth
    :param problem:
    The problem model object
    :return:
    The results of the search, either the found solution
    or a failure
    """
    depth = 0
    while depth >= 0:
        result = depth_limited_search(problem, depth)
        if result != problem.cutoff:
            return result
        depth += 1
