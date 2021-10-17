X = "X"
O = "O"
EMPTY = None


import math
import numpy as np
import copy


def xo_state(board) :
    """
    returns the number of x&o in the board

    output list of [ x_no , o_no ]
    """
    x = 0
    o = 0
    for i in range (3) :
        for j in range (3) : 
            if board[i][j] == X :
                x = x + 1 
            if board[i][j] == O :
                o = o + 1 
    
    return  [ x , o ]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # always x starts
    x , o = xo_state(board)
    if x == 0 or x<=o : 
        return X
    else :
        return O 


    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3) :
        for j in range(3) :
            if board[i][j] is EMPTY :
                actions.add((i,j))
    return actions
    raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # to know the player which will play either X or O
    plyr = player(board)

    # make a copy of the board so you dont change the existing board
    board_copy = copy.deepcopy(board)

    board_copy[action[0]][action[1]] = plyr

    return board_copy
    
    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None
   

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    x , o = xo_state(board)
    print(x)
    print(o)
    print(winner(board))
    if winner(board) is X or  winner(board) is O :
        return True
    elif x+o == 9 : 
        return True
    return False
         
    raise NotImplementedError


b = [[X, X, O],
     [O, O, X],
     [X, O, X]]

print(terminal(b))