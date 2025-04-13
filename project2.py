#Add a win condition checker to determine when someone wins.

#prevent the game from continuing when the board is full (detect a draw).

from random import randrange # importing randrange function to make the computer choose random moves

def display_board(board):
    for i in board:
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print(f'|   {i[0]}   |   {i[1]}   |   {i[2]}   ')
        print('|       |       |       |')
        print('+-------+-------+-------+')

board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
    ]

def check_win(board, symbol):
    for row in board:
        if row[0] == symbol and row[1] == symbol and row[2] == symbol:
            return True
    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol or \
       board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False

def is_draw(board):
    for row in board:
        for col in row:
            if isinstance(col, int):
                return False
    return True


player_turn = True # player goes first (true), (false = computer´s turn)

# game loop that continues until the game ends
while True:
    display_board(board)  # show the current state of the board

    # player's turn
    try:
        O = int(input('Make your move choosing a number in the board: '))

        # check if the input is valid
        if O < 1 or O > 9:
            print('Please, pick another available number.')
            continue # if the number is not valid, ask again

        player_turn = False
        # loop through the board to check if the spot is available
        for i in range(3):
            for j in range(3):
                if board[i][j] == O:
                    board[i][j] = 'O'
                    player_turn = True # set for true beacuse the move was made
                    break # exit the inner loop once the move is made
            if player_turn:
                break  # exit outer loop once move is made

        if not player_turn:
            print('This move has already been ocupied.')
            continue # ask again for another move
    
    except:
        print('Please choose a valid number.')
        continue

    if check_win(board, 'O'):
        print('Player wins!')
        break

    if is_draw(board):
        print('It´s a draw!')
        break


    # computer´s turn
    while True:
        # generate a random number between 1 and 9 for the computer's move
        X = randrange(1, 10)
    
        player_turn = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    board[i][j] = 'X'
                    player_turn = True
                    break
            if player_turn:
                break  # exit loop once move is made
        if player_turn:
            break  # exit loop once a valid move is made

    if check_win(board, 'X'):
        print('Computer wins!')
        break

    if is_draw(board):
        print('It´s a draw!')
        break

    display_board(board)
    
    