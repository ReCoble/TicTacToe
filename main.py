import time
from random import randrange

board = [[1,2,3],[4,5,6],[7,8,9]]

def display_board(board):
    print("+-------+--------+-------+")
    print("|       |        |       |")
    print("|  " , board[0][0] ,   "  |   " , board[0][1] ,  "  |   " , board[0][2] ,   " |")
    print("|       |        |       |")
    print("+-------+--------+-------+")
    print("|       |        |       |")
    print("|  " , board[1][0] , "  |   " , board[1][1] , "  |  " , board[1][2] , "  |")
    print("|       |        |       |")
    print("+-------+--------+-------+")
    print("|       |        |       |")
    print("|  " , board[2][0] , "  |   " , board[2][1] , "  |   " , board[2][2] , " |")
    print("|       |        |       |")
    print("+-------+--------+-------+")



def enter_move(board):
    display_board(board)
    try:
        users_row = int(input("Choosing the row. Please enter a number from 0 to 2 here: "))
        if users_row == 0  or users_row == 1 or users_row == 2:
            invalid_entry = False
        else:
            invalid_entry = True
        while invalid_entry == True:
            print("You entered ", users_row, ". Value must be 0 , 1 or 2. Please try again.")
            users_row = int(input("Choosing the row. Please enter a number from 0 to 2 here: "))
            if users_row != 0 or users_row != 1 or users_row != 2:
                invalid_entry = True

    except ValueError:
        print("Wrong value entered. Please enter a int.")
        error = True
        while error:
            try:
                users_row = int(input("Choosing the row. Please enter a number from 0 to 2 here: "))
                if users_row == 0 or users_row == 1 or users_row == 2:
                    invalid_entry = False
                else:
                    invalid_entry = True
                while invalid_entry == True:
                    print("You entered ", users_row, ". Value must be 0 , 1 or 2. Please try again.")
                    users_row = int(input("Choosing the row. Please enter a number from 0 to 2 here: "))
                    if users_row != 0 or users_row != 1 or users_row != 2:
                        invalid_entry = True
                error = False
            except ValueError:
                print("Wrong value entered. Please enter a int.")
                error = True

    try:
        users_column = int(input("Choosing the column. Please enter a number from 0 to 2 here: "))
        if users_column == 0 or users_column == 1 or users_column == 2:
            invalid_entry = False
        else:
            invalid_entry = True
        while invalid_entry == True:
            print("You entered ", users_column, ". Value must be 0 , 1 or 2. Please try again.")
            users_column = int(input("Choosing the column. Please enter a number from 0 to 2 here: "))
            if users_column == 0 or users_column == 1 or users_column == 2:
                invalid_entry = False

    except ValueError:
        print("Wrong value entered. Please enter a int.")
        error = True
        while error:
            try:
                users_column = int(input("Choosing the column. Please enter a number from 0 to 2 here: "))
                if users_column == 0 or users_column == 1 or users_column == 2:
                    invalid_entry = False
                else:
                    invalid_entry = True
                while invalid_entry == True:
                    print("You entered ", users_column, ". Value must be 0 , 1 or 2. Please try again.")
                    users_column = int(input("Choosing the column. Please enter a number from 0 to 2 here: "))
                    if users_column == 0 or users_column == 1 or users_column == 2:
                        invalid_entry = False
                error = False
            except ValueError:
                print("Wrong value entered. Please enter a int.")
                error = True



    if board[users_row][users_column] == "X" or board[users_row][users_column] == "O":
        print("Place chosen has been taken already. Please choose another.")
        enter_move(board)
    else:
        board[users_row][users_column] = "O"
    return board
  


def make_list_of_free_fields(board):
    # board = [[1, 2, 3], [4, "O", 6], [7, 8, 9]]
    row_num = 0
    free_spaces2 = []
    for row in board:
        col_num = 0
        for col in row:
            if type(col) == int:
                free_spaces2.append([row_num,col_num])
                free_spaces = tuple(free_spaces2)
            col_num += 1
        row_num += 1
    print(free_spaces)


def victory_for(board, sign):
    row_position = 0
    players_positions = []
    victory = False
    for row in board:
        count = 0
        for i in row:
            if i == sign:
                count = count + 1
        if count == 3:
            print("Player with ", sign, " has won!")
            victory = True
            break

        col_position = 0
        for col in row:
            if sign == col:
                players_positions.append(board[row_position][col_position])

            col_position = col_position + 1

        row_position = row_position + 1
    for row in board:
        for col in range(len(row)):
            if board[0][col] in players_positions and board[1][col] in players_positions \
                    and board[2][col] in players_positions:
                print("Player with ", sign, " has won!")
                victory = True
                break
        if victory:
            break

        if board[0][0] in players_positions and board[1][1] in players_positions and board[2][2] in players_positions:
            print("Player with ", sign, " has won!")
            victory = True
            break
        elif board[0][2] in players_positions and board[1][1] in players_positions and board[2][0] in players_positions:
            print("Player with ", sign, " has won!")
            victory = True
            break

        if victory:
            break

    return victory



def draw_move(board):
    stop = False
    if board[1][1] == 5:
        board[1][1] = "X"
    else:
        for i in range(3):
            column = randrange(3)
            if board[i][column] == "X" or board[i][column] == "O":
                for t in range(3):
                    column = randrange(3)
                    if board[i][column] == "X" or board[i][column] == "O":
                        continue
                    else:
                        board[i][column] = "X"
                        stop = True
                        break
            else:
                board[i][column] = "X"
                break
            if stop == True:
                break
    return board


board = [[1,2,3],[4,5,6],[7,8,9]]

print("                                 Tic Tac Toe \n")
print("The objective of the game is to get three in a row. The computer always goes first.")
print("To play, you will enter one number from 0 to 2, inclusively, for the row then another number from 0 to 2 "
      ",inclusively, for the column.")
print("0 is the first row/column, 1 is the second and 2 is the third.")
time.sleep(10)
print("Below is the game board. \n")

display_board(board)
time.sleep(5)
print("Let's play! \n")


game_ending = False
while game_ending is not True:
    if not game_ending:
        game_ending = victory_for(board, 'X')
        if game_ending:
            break
    print("Computer's turn.")
    time.sleep(2)
    board = draw_move(board)
    display_board(board)
    game_ending = victory_for(board, 'O')
    if not game_ending:
        game_ending = victory_for(board, 'X')
        if game_ending:
            break
    print("Your turn.")
    print("These are all of the free spaces you can use.")
    make_list_of_free_fields(board)
    board = enter_move(board)
    display_board(board)
    time.sleep(1)
    game_ending = victory_for(board, 'O')
    if not game_ending:
        game_ending = victory_for(board, 'X')

