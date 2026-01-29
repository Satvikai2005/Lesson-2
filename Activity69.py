
boards = {'7':' ','8':' ','9':' ', 
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '}

board_keys = list(boards.keys())

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(boards)
        print("It's your turn, " + turn + ". Move to which place (1-9)?")
        
        move = input()
        if move not in boards:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        if boards[move] == ' ':
            boards[move] = turn
            count += 1 
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        if count >= 5:
            win_cond = [
                ['7','8','9'], ['4','5','6'], ['1','2','3'], 
                ['7','4','1'], ['8','5','2'], ['9','6','3'], 
                ['7','5','3'], ['9','5','1']                
            ]
            
            winner = False
            for combo in win_cond:
                if boards[combo[0]] == boards[combo[1]] == boards[combo[2]] != ' ':
                    print_board(boards)
                    print("\nGame Over.\n")                
                    print(" **** " + turn + " won! ****")
                    winner = True
                    break
            if winner: break

        if count == 9:
            print_board(boards)
            print("\nGame Over.\n")
            print("It's a tie.")
            break
        turn = 'O' if turn == 'X' else 'X'

    restart = input("Do you want to play again (y/n)? ")
    if restart.lower() == "y":
        for key in board_keys:
            boards[key] = " "
        game()

if __name__ == "__main__":
    game()