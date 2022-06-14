
def evaluate(board):
    if ('xxx' in board):
        result ='x' # The player who uses crosses (Xs) has won
    elif ('ooo' in board): 
        result ='o' # The player who uses noughts (Os) has won
    elif ('-' not in board): 
        result ='!'  # Draw (the board is full but nobody has won)
    else:
        result = '-' #Rest (i.e. the game is not finished)
    return result

def move(board, mark, position): # Returns the game board with the given mark in the given position.
    move_on_board = board[:position - 1] + mark + board[position + 1:]
    return move_on_board


def player_move(board, position):
    new_position = int(input('What position number do you choose?'))
    while True:
        if new_position<1:
            print ('You cannot use a negative number')
            int(input('What position number do you choose?'))
        elif new_position>20:
            print ('The number is too big')
            int(input('What position number do you choose?'))
        elif '-' not in board[new_position]:
            print('The spot is taken, try again')
            int(input('What position number do you choose?'))
        else:
            board = move(board, 'x', new_position)
        break
    return board

from random import randrange
from turtle import position
def pc_move(board): # Returns a game board with the computer's move.
    pc_position = randrange(19)
    while True:
        if board[pc_position] == "x":
            pc_position = randrange (19)
        elif board[pc_position] == "o":
            pc_position = randrange (19)
        elif board[pc_position] == "-":
            board = move(board, 'o', pc_position)
        break
    return board


def tictactoe():
    board = ('-' * 20)
    print(board)
    while '-' in board:
        board = player_move(board, position)
        print(board)
        print(evaluate(board))
        board = pc_move(board)
        print(board)
        print(evaluate(board))
    
print(tictactoe())