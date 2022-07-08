def evaluate(board):
    if 'XXX' in board:
        return 'X'    #user won
    elif 'OOO' in board: 
        return'O'  #PC won
    elif '-' not in board:
        return '!'   #the board is full
    else:
        return '-'   #game continues
   

def move(board, mark, position): # Returns the game board with the given mark in the given position.
    move_on_board = board[:position - 1] + mark + board[position:]
    return move_on_board


def player_move(board): # Returns a game board with the player's move.
    while True:
        position = int(input('Please choose position number between 1 and 20: '))
        if position<1:
            print ('You cannot use a negative number')
        elif position>20:
            print ('The number is too big')
        elif '-' not in board[position-1]:
            print('The spot is taken, try again')
        else:
            board = move(board, 'X', position)
            return board

from random import randrange

def pc_move(board): # Returns a game board with the computer's move.
    while True:
        pc_position = randrange(1, 21)
        if board[pc_position-1] == "-":
            board = move(board, 'O', pc_position)
        else: 
            pc_position = randrange(1, 21)
            board = move(board, 'O', pc_position)
        return board


def tictactoe():
    print('Hello player! This is a tic tac toe game where you play against the computer')
    print('You play as "X"')
    print('Good luck!')
    board = ('-' * 20)
    print('Here\'s the board: ' + board)
    while True:
        board = player_move(board)
        if evaluate(board) == '!':
            print()
            print('No more spaces ' + board)
            break
        elif evaluate(board) == 'X':
            print('Congrats, you won!')
            print('Here\'s the final board:' + board)
            break
        elif evaluate(board) == 'O':
            print('Sorry, computer won')
            print('Here\'s the final board:' + board)
            break
        else:
            print("Your move: " + board)
            

        board = pc_move(board)
        if evaluate(board) == '!':
            print()
            print('No more spaces ' + board)
            break
        elif evaluate(board) == 'X':
            print('Congrats, you won!')
            print('Here\'s the final board:' + board)
            break
        elif evaluate(board) == 'O':
            print('Computer won')
            print('Here\'s the final board:' + board)
            break
        else:
            print("PC move: " + board)
    
tictactoe()