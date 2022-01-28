print("TicTacToe!\n")

#Declare Variables

row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
winner = False
player1 = "Player1"
player2 = "Player2"
turnCount = 0


while winner != True:

    #Set pieces to false
    xPiece = False
    oPiece = False

    #row1
    print(row1[0] + " | " + row1[1] + " | " + row1[2])

    print("---------")
    #row2
    print(row2[0] + " | " + row2[1] + " | " + row2[2])

    print("---------")
    #row3
    print(row3[0] + " | " + row3[1] + " | " + row3[2])


    #Determine player's turn
    if turnCount % 2 == 0:
        print(f"{player1}'s turn")
        xPiece = True
        #winner = True
        turnCount = turnCount + 1
        
    else:
        print(f"{player2}'s turn")
        oPiece = True
        #winner = True
        turnCount = turnCount + 1
        
        #"""
        if xPiece == True:
            selection = input(f"Make your move {player1}: ")
            piecePlacement = "x"
        else:
            oPiece = True
            selection = input(f"Make your move {player2}: ")
            piecePlacement = "o"

        if selection == 1 and (row1[0] != 'x' and row1[0] != 'o'):
            row1[0] = piecePlacement

        else:#"""
            break




