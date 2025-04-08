from random import randrange


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


move_choose = []
player_turn = True

while True:
    display_board(board)

    try:
        O = int(input('Make a move selecting a number in the board: '))
        
        if O > 9 or O < 1:
            print('Try again another number.')
            continue

        player_turn = True
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O' or board[i][j] == 'X':
                    print("This spot is already taken. Choose another.")
                    O = int(input('Make a move selecting a number in the board: '))
                    continue

                if board[i][j] == O:
                    board[i][j] = 'O'
                    player_turn = False
                    break
        
        X = randrange(1, 10)
        player_turn = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O' or board[i][j] == 'X':
                    X = randrange(1, 10)
                    continue

                if board[i][j] == X:
                    board[i][j] = 'X'
                    player_turn = True
                    break
            
        move_choose.append(O)
        display_board(board)

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 9.")
