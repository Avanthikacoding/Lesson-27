board = [" " for _ in range(9)]
player = "X"
turns = 0

while turns < 9:
    print("\n" + board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    a = "Player ", player , " pick a point (1-9): "
    move = int(input(a)) - 1
    if board[move] == " ":
        board[move] = player
        turns += 1
        if (board[0] == board[1] == board[2] != " " or  
            board[3] == board[4] == board[5] != " " or  
            board[6] == board[7] == board[8] != " " or  
            board[0] == board[3] == board[6] != " " or  
            board[1] == board[4] == board[7] != " " or 
            board[2] == board[5] == board[8] != " " or  
            board[0] == board[4] == board[8] != " " or 
            board[2] == board[4] == board[6] != " "):  
            print("Player {player} wins!")
            break
        player = "O" if player == "X" else "X"
    else:
        print("Point already taken, try again!")

if turns == 9:
    print("It's a draw!")
