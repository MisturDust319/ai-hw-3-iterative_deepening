import numpy as np
import random

__name__ == "__main__"

print(np.__version__)

def apply_action(board,action):

    deltas = np.array([[-1,0,1,0],[0,1,0,-1]])
    action_2_index = {'up':0,'right':1,'down':2,'left':3}
    # dictionary matching direction to number value
    posx,posy = np.where(np.isin(board, [0]))
    # isin: compares all members of board to [0] and returns array of bools
    # positioned according to the corresponding board pieces
    # where:

    (x,y) = (posx[0],posy[0])
    (new_x,new_y) = (x + deltas[0,action_2_index[action]],y + deltas[1,action_2_index[action]])

    try:
        el = board[new_x,new_y]
        board[x,y] = el
        board[new_x,new_y] = 0
       # print(new_x, new_y)
       # print(board)
    except IndexError:
        pass
    return board


def goal_test(board):
    goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    return np.array_equal(board,goal)


def n_out_of_order(board):
    goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    return np.count_nonzero(np.subtract(board,goal))


def mess_up(board,actions,moves):

    for iter in range(0,moves):
        board = apply_action(board,actions[random.randint(0,3)])
    pass


def random_search(board):
    # create a sequce of 32 random moves and keep going until it is solved.
    # this may take a long time to return

    new_board = np.copy(board)
    actions = ["up", "right", "down", "left"]
    while True:
        sequence = []
        new_board = np.copy(board)
        for iteration in range(0,32):
            action = actions[random.randint(0,3)]
            sequence.append(action)
            new_board=apply_action(new_board, action)
            if goal_test(new_board):
                return sequence
    pass


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
