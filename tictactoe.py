"""
Tic Tac Toe Player
"""

import math
import numpy as np
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

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

    if board_copy[action[0]][action[1]] is not EMPTY :
        raise "onvalid play"
    

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
    
    if winner(board) is X or  winner(board) is O :
        return True
    elif x+o == 9 : 
        return True
    return False
         
    raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X :
        return 1
    elif winner(board) == O : 
        return -1
    else : 
        return 0
    raise NotImplementedError

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) :
        return None
 
    # get who will play the next play
    pl = player(board)

    if pl == X :
        val , move = max_value(board)
        return move
    if pl == O : 
        val , move = min_value(board)
        return move




    raise NotImplementedError
