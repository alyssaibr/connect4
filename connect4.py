getimport random
import math


def menu():
    print('Welcome to Connect4!')
    while True:  # player decides number of rows
        try:
            rows = int(input('How many rows would you like to play with? 6 or 7: '))

            if rows == 6:
                board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0,
                         0, 0, 0,
                         0, 0, 0, 0, 0, 0]  # list with 42 elements
                break
            elif rows == 7:
                board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0,
                         0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # list with 49 elements
                break
            else:
                print(
                    'Please enter only 6 or 7!')  # if player enters integer not 6 or 7, it will ask player to input again
        except (ValueError, NameError):  # if player inputs a string
            print('Please enter only 6 or 7!')
            continue

    while True:  # set up conditions of game
        opp = input('Would you like to play with the computer (1) or a friend (2) ?: ')
        if opp == '1':
            while True:
                level = input('Difficulty level 1 or 2: ')
                if level == '1':
                    print('The game will start now. Have fun!')
                    break
                elif level == '2':
                    print('The game will start now. Have fun!')
                    break
                else:
                    print('Please enter 1 for computer or 2 for friend!')
                    continue
                break

        elif opp == '2':
            print('The game will start now. Have fun!')
            break
        else:
            print('Please enter only 1 or 2! ')
            continue
        break
    display_board(board)

    # start of game
    # initialise variables
    pop = False
    turn = random.randint(1, 2)  # randomly chooses who goes first
    who_played = 0
    if opp == '2':  # 2-player game
        while check_victory(board, who_played) == 0:
            while True:
                while True:
                    try:
                        col_select = int(
                            input(f'Player {turn}, Select column 1-7: ')) - 1  # index of column = player's choice - 1
                        if col_select < 0 or col_select > 6:
                            print('Please enter 1 to 7 only!')
                            break
                        else:
                            break
                    except (ValueError, NameError):
                        print('Please enter 1 to 7 only!')

                while True:
                    try:
                        pop = int(input('Would you like to pop from below(1) or drop from above(2) ?: '))
                        if pop == 1:
                            pop = True
                            break
                        elif pop == 2:
                            pop = False
                            break
                        else:
                            print('Please enter only 1 or 2!')
                    except (ValueError, NameError):
                        print('Please enter only 1 or 2!')
                if check_move(board, turn, col_select, pop):
                    board = apply_move(board, turn, col_select, pop)
                    display_board(board)
                    turn = turn % 2 + 1
                    break
                else:
                    print('Invalid move! Please try again')
                    continue

        else:  # if player 1/2 wins, game ends
            print(f'Player {check_victory(board, who_played)} wins!')

            while True:  # player chooses to play again or exit game
                try:
                    play_again = input('Press 1 to play again or 2 to exit the game: ')
                    if play_again == '1':
                        menu()
                    elif play_again == '2':
                        print('Bye bye!')
                        break
                    else:
                        print('Please enter 1 or 2 only!')
                except (ValueError, NameError):
                    print('Please enter 1 or 2 only!')

    if opp == '1':  # player-CPU game
        while check_victory(board, who_played) == 0:
            while turn == 1:  # player's turn
                while True:
                    while True:
                        try:
                            col_select = int(
                                input(
                                    f'Player {turn}, Select column 1-7: ')) - 1  # index of column = player's choice - 1
                            if col_select < 0 or col_select > 6:
                                print('Please enter 1 to 7 only!')
                                break
                            else:
                                break
                        except (ValueError, NameError):
                            print('Please enter 1 to 7 only!')

                    while True:
                        try:
                            pop = int(input('Would you like to pop from below(1) or drop from above(2) ?: '))
                            if pop == 1:
                                pop = True
                                break
                            elif pop == 2:
                                pop = False
                                break
                            else:
                                print('Please enter only 1 or 2!')
                        except (ValueError, NameError):
                            print('Please enter only 1 or 2!')
                    if check_move(board, turn, col_select, pop):
                        board = apply_move(board, turn, col_select, pop)
                        display_board(board)
                        turn = 2  # change turn
                        break
                    else:
                        print('Invalid move! Please try again')
                        continue

            else:  # CPU's turn
                print("Player 2 (CPU) 's turn")
                # computer move function returns 2 variables; column is first variable (index 0),
                # pop is second variable (index 1)
                col = computer_move(board, turn, level)[0]
                pop = computer_move(board, turn, level)[1]
                board = apply_move(board, turn, col, pop)
                display_board(board)
                turn = 1  # change turn

        else:
            if check_victory(board, who_played) == 1:
                print('Player 1 wins!')
            else:
                print('CPU wins!')
            while True:
                try:
                    play_again = input('Press 1 to play again or 2 to exit the game: ')
                    if play_again == '1':
                        menu()
                    elif play_again == '2':
                        print('bye bye!')
                        break
                    else:
                        print('Please enter 1 or 2 only!')
                except (ValueError, NameError):
                    print('Please enter 1 or 2 only!')


def check_move(board, turn, col, pop):
    rows = int(len(board) / 7)
    if pop:
        if board[col] == turn:  # player can only pop a disc that belongs to them
            return True
        else:  # invalid move, player chooses again
            return False
    if not pop:
        for i in range(rows):
            if board[7 * i + col] == 0:  # checks for empty slots along a column
                return True
                break
            else:
                continue


def apply_move(board, turn, col, pop):
    rows = int(len(board) / 7)
    board = board.copy()

    if pop:
        for i in range(rows - 1):
            if i == 0:
                board[7 * i + col] = 0

            board[7 * i + col] = board[7 * (i + 1) + col]
            # discs fall 1 row down, slot becomes occupied by the disc previously above it

    else:
        for i in range(rows):
            if board[7 * i + col] == 0:
                board[7 * i + col] = turn  # slot becomes occupied by player
            else:
                continue
            break

    return board


def check_victory(board, who_played):
    # initial condition: player 1 and 2 have not won yet
    player1 = False
    player2 = False
    rows = int(len(board) / 7)

    # horizontal
    for i in range(0, rows):
        for j in range(0, 4):
            if board[7 * i + j] == board[7 * i + j + 1] == board[7 * i + j + 2] == board[7 * i + j + 3] == 1:
                player1 = True
            if board[7 * i + j] == board[7 * i + j + 1] == board[7 * i + j + 2] == board[7 * i + j + 3] == 2:
                player2 = True

    # vertical
    for i in range(0, 7):
        for j in range(0, rows - 3):
            if board[i + 7 * j] == board[i + 7 * (j + 1)] == board[i + 7 * (j + 2)] == board[i + 7 * (j + 3)] == 1:
                player1 = True
            if board[i + 7 * j] == board[i + 7 * (j + 1)] == board[i + 7 * (j + 2)] == board[i + 7 * (j + 3)] == 2:
                player2 = True

    # diagonal (to the right): discs are 8 indexes away from one another
    for i in range(0, rows - 3):
        for j in range(0, 4):
            if board[i * 7 + j] == board[i * 7 + j + 8] == board[i * 7 + j + 16] == board[i * 7 + j + 24] == 1:
                player1 = True
            if board[i * 7 + j] == board[i * 7 + j + 8] == board[i * 7 + j + 16] == board[i * 7 + j + 24] == 2:
                player2 = True

    # diagonal (to the left): discs are 6 indexes away from one another
    for i in range(0, rows - 3):
        for j in range(3, 7):
            if board[i * 7 + j] == board[i * 7 + j + 6] == board[i * 7 + j + 12] == board[i * 7 + j + 18] == 1:
                player1 = True
            if board[i * 7 + j] == board[i * 7 + j + 6] == board[i * 7 + j + 12] == board[i * 7 + j + 18] == 2:
                player2 = True

    if not player1 and not player2:  # no one wins
        return 0
    if player1 and not player2:  # player 1 wins
        return 1
    if not player1 and player2:  # player 2 wins
        return 2
    if player1 and player2:  # both win
        if who_played == 1:  # e.g. player 1 makes a move that causes both to win, player 2 wins
            return 2
        else:  # likewise for player 2
            return 1


def computer_move(board, turn, level):
    if level == '1':
        col = random.randint(0, 6)  # chooses a random column to make a move in
        pop = bool(random.randint(0, 1))  # randomly decides to pop or drop a disc
        return col, pop
    else:
        copy_board = board.copy()  # copy of the board to test winning conditions without changing the actual board

        # this loop tests if a move made by the CPU will result in CPU win, move will be applied
        for i in range(7):
            pop = False
            if check_move(copy_board, turn, i, pop):  # checks if move is valid first
                copy_board = apply_move(copy_board, turn, i, pop)
                who_played = turn
                if check_victory(copy_board, who_played) == turn:
                    return i, False

        # this loop tests if a move made by the human will result in human win, CPU applies the same move to prevent
        # human from winning
        for i in range(7):
            pop = False
            if turn == 1:
                opp = 2
            else:
                opp = 1
            if check_move(copy_board, turn, i, pop):
                copy_board = apply_move(copy_board, turn, i, pop)
                who_played = turn
                if check_victory(copy_board, who_played) == opp:
                    return i, False


def display_board(board):  # prints chosen no. of rows of 7 zeroes
    rows = int(len(board) / 7)
    if rows == 6:
        zeroes = 42
        topleftzero = 35
    if rows == 7:
        zeroes = 49
        topleftzero = 42

    for x in range(rows, 0, -1):  # reverse index
        index = (rows - x) * 7
        print([board[i] for i in range(topleftzero - index, zeroes - index)])


if __name__ == "__main__":
    menu()
