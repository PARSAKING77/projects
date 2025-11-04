
board = [' ' for _ in range(9)]

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    while True:
        move = input("Player {}. Enter your move (1-9): ".format(number))
        if move in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            move = int(move)
            if board[move - 1] == ' ':
                board[move - 1] = icon
                break
            else:
                print("That space is taken!")
        else:
            print("Invalid move!")

def check_win():
    winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for position in winning_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] != ' ':
            return True
    return False

def main():
    while True:
        player_move('X')
        print_board()
        if check_win():
            print("Player X wins!")
            break
        player_move('O')
        print_board()
        if check_win():
            print("Player O wins!")
            break

main()