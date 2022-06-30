def evaluate(board):
    if 'XXX' in board:
        result ='X won'   
    elif 'OOO' in board: 
        result ='O won' 
    elif '-' not in board: 
        result ='Draw! The board is full'  
    else:
        result = 'Please continue playing' 
    return result

def move(board, mark, position): # Returns the game board with the given mark in the given position.
    move_on_board = board[:position - 1] + mark + board[position:]
    return move_on_board


def player_move(board):
    while True:
        position = int(input('What position number do you choose? '))
        if position<1:
            print ('You cannot use a negative number')
        elif position>20:
            print ('The number is too big')
        elif '-' not in board[position]:
            print('The spot is taken, try again')
        else:
            board = move(board, 'X', position)
            return board

from random import randrange

def pc_move(board): # Returns a game board with the computer's move.
    while True:
        pc_position = randrange(1, 21)
        if board[pc_position] == "X":
            pc_position = randrange(1,21)
        elif board[pc_position] == "O":
            pc_position = randrange(1,21)
        elif board[pc_position] == "-":
            board = move(board, 'O', pc_position)
        return board

def tictactoe():
    print('Hello player! This is a tic tac toe game where you play against computer')
    print('Good luck!')
    board = ('-' * 20)
    print(board)
    while True:
        board = player_move(board)
        result = evaluate(board)
        if result == 'Please continue playing':
            print('Game contiues')
            print('Your move: ' + board)
        elif result == 'X won':
            print('Congrats, you won!')
        elif result == 'O won':
            print('Sorry, computer won')
        else:
            print(board)
            break

        board = pc_move(board)
        result = evaluate(board)
        if result == 'Please continue playing':
            print('Game contiues')
            print('Computer move: ' + board)
        else:
            print(board)
            break
    
tictactoe()