def evaluate(board):
    if 'xxx' in board:
        result ='x' # The player who uses crosses (Xs) has won
    elif 'ooo' in board: 
        result ='o' # The player who uses noughts (Os) has won
    elif '-' not in board: 
        result ='!'  # Draw (the board is full but nobody has won)
    else:
        result = '-' #Rest (i.e. the game is not finished)
    return result

def move(board, mark, position): # Returns the game board with the given mark in the given position.
    move_on_board = board[:position - 1] + mark + board[position + 1:]
    return move_on_board


def player_move(board, position):
    while True:
        if position<1:
            print ('You cannot use a negative number')
            int(input('What position number do you choose?'))
        elif position>20:
            print ('The number is too big')
            int(input('What position number do you choose?'))
        elif '-' not in board[position]:
            print('The spot is taken, try again')
            int(input('What position number do you choose?'))
        else:
            board = move(board, 'x', position)
        break
    return board

from random import randrange


def pc_move(board): # Returns a game board with the computer's move.
    pc_position = randrange(1,21)
    while True:
        if board[pc_position] == "-":
            board = move(board, 'o', pc_position)
        else:
            pc_position = randrange(1,21)
        break
    return board

def tictactoe():
    board = ('-' * 20)
    print(board)
    while True:
        board = player_move(board, int(input('What position number do you choose?')))
        print(board)
        result = evaluate(board)
        if result== '-':
            print(result)
        else:
            break
        board = pc_move(board)
        print(board)
        result = evaluate(board)
        if result == '-':
            print(result)
        else:
            break
    
print(tictactoe())