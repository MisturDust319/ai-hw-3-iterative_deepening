from eight_puzzle import *
from iterative_deepening import *

__name__ == "__main__"

print(np.__version__)

def main():

    board = np.array([[1, 2, 3], [4, 5,6], [7, 8,0]])
    print(goal_test(board))
    actions = ["up","right","down","left"]
    mess_up(board, actions, 10)
    print(board)
    print(n_out_of_order(board))
    print(goal_test(board))
    print(random_search(board))
    pass


if __name__ == "__main__":
    main()
