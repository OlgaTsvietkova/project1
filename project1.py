# board = ('-' * 20)
# mark = input('Please write your mark ("o" or "x"): ')
# position = int(input('Choose a number from 1 to 20: '))


def evaluate(board):
    board = ('-' * 20)
    if ('xxx' in board):
        print('x') # The player who uses crosses (Xs) has won
    elif ('ooo' in board): 
        print('o') # The player who uses noughts (Os) has won
    elif ('-' not in board): 
        print('!')  # Draw (the board is full but nobody has won)
    else:
        print('-') #Rest (i.e. the game is not finished)

def move(board, mark, position):
    board = ('-' * 20)
    # Returns the game board with the given mark in the given position.
    return print(board[:position - 1] + mark + board[position + 1:])

def player_move(board, position):
    board = ('-' * 20)
    while True:
        if position<1:
            print ('You cannot use a negative number')
        elif position>20:
            print ('The number is too big')
        elif '-' not in board[position]:
            print('The spot is taken, try again')
        else:
            return move(board, 'x', position)
        break

def pc_move(board):
    # Returns a game board with the computer's move.
    from random import randrange
    board = ('-' * 20)
    position = randrange(19)
    while '-' in board:
        if '-' in board:
            return move(board, 'o', position)
        break

  
def tictactoe():
    board = ('-' * 20)
    print(board)
    while '-' in board:
        board = player_move(board, int(input('Choose a number from 1 to 20: ')))
        print(board)
        board = pc_move(board)
        print(board)
        evaluate(board)
    
tictactoe()
