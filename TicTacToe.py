from distutils.dir_util import copy_tree


print("TicTacToe!\n")

#Initialize Variables

row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
winner = False
player1 = "Player1"
player2 = "Player2"
turnCount = 0
play = True  
playAgainValid = False 



def winner_Calc():
    
    #Player 1 checks
    
    #Horizontal Checks for Player 1
    if 'x' == row1[0] and 'x' == row1[1] and 'x' == row1[2]:
        print(f"{player1} wins!")
        winner = True
        return(winner)
    elif 'x' == row2[0] and 'x' == row2[1] and 'x' == row2[2]:
        print(f"{player1} wins!")
        winner = True
        return(winner)        
    elif 'x' == row3[0] and 'x' == row3[1] and 'x' == row3[2]:
        print(f"{player1} wins!")
        winner = True
        return(winner)
    #Diagonal Checks for Player 1
    elif 'x' == row1[0] and 'x' == row2[1] and 'x' == row3[2]:
        print(f"{player1} wins!")
        winner = True
        return(winner)
    elif 'x' == row1[2] and 'x' == row2[1] and 'x' == row3[0]:
        print(f"{player1} wins!")
        winner = True
        return(winner)

    #Vertical checks for Player 1
    elif 'x' == row1[0] and 'x' == row2[0] and 'x' == row3[0]:
        print(f"{player1} wins!")
        winner = True
        return(winner)        
    elif 'x' == row1[1] and 'x' == row2[1] and 'x' == row3[1]:
        print(f"{player1} wins!")
        winner = True
        return(winner)
    elif 'x' == row1[2] and 'x' == row2[2] and 'x' == row3[2]:
        print(f"{player1} wins!")
        winner = True
        return(winner)    

    
    #Player 2 checks
    
    #Horizontal Checks for Player 2
    if 'o' == row1[0] and 'o' == row1[1] and 'o' == row1[2]:
        print(f"{player2} wins!")
        winner = True
        return(winner)
    elif 'o' == row2[0] and 'o' == row2[1] and 'o' == row2[2]:
        print(f"{player2} wins!")
        winner = True
        return(winner)        
    elif 'o' == row3[0] and 'o' == row3[1] and 'o' == row3[2]:
        print(f"{player2} wins!")
        winner = True
        return(winner)
    #Diagonal Checks for Player 2
    elif 'o' == row1[0] and 'o' == row2[1] and 'o' == row3[2]:
        print(f"{player2} wins!")
        winner = True
        return(winner)
    elif 'o' == row1[2] and 'o' == row2[1] and 'o' == row3[0]:
        print(f"{player2} wins!")
        winner = True
        return(winner)

    #Vertical checks for Player 2
    elif 'o' == row1[0] and 'o' == row2[0] and 'o' == row3[0]:
        print(f"{player2} wins!")
        winner = True
        return(winner)        
    elif 'o' == row1[1] and 'o' == row2[1] and 'o' == row3[1]:
        print(f"{player2} wins!")
        winner = True
        return(winner)
    elif 'o' == row1[2] and 'o' == row2[2] and 'o' == row3[2]:
        print(f"{player2} wins!")
        winner = True
        return(winner)  




#Loop to control playing again
while play == True:   

    row1 = ["1", "2", "3"]
    row2 = ["4", "5", "6"]
    row3 = ["7", "8", "9"]
    winner = False
    player1 = "Player1"
    player2 = "Player2"
    turnCount = 0
    play = True  
    playAgainValid = False 


    while True:

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
        print(row3[0] + " | " + row3[1] + " | " + row3[2] + "\n")


        #Calculate Winner!
        if winner_Calc() == True:
            break
        
        elif turnCount == 9 and winner != True:
            print("Cat wins!")
            break

        #Determine player's turn
        if turnCount % 2 == 0:
            print(f"{player1}'s turn \n")
            xPiece = True
            turnCount = turnCount + 1
            
        else:
            print(f"{player2}'s turn \n")
            oPiece = True
            turnCount = turnCount + 1
        #end if

        #piece selection
        if xPiece == True:
            selection = input(f"Make your move {player1}: ")
            piecePlacement = "x"
        else:
            oPiece = True
            selection = input(f"Make your move {player2}: ")
            piecePlacement = "o"
        
        
        
        #mark the board with piece    
        if selection == '1' and (row1[0] != 'x' and row1[0] != 'o'):
            row1[0] = piecePlacement
            
        elif selection == '2' and (row1[1] != 'x' and row1[1] != 'o'):
            row1[1] = piecePlacement

        elif selection == '3' and (row1[2] != 'x' and row1[2] != 'o'):
            row1[2] = piecePlacement
        
        elif selection == '4' and (row2[0] != 'x' and row2[0] != 'o'):
            row2[0] = piecePlacement

        elif selection == '5' and (row2[1] != 'x' and row2[1] != 'o'):
            row2[1] = piecePlacement

        elif selection == '6' and (row2[2] != 'x' and row2[2] != 'o'):
            row2[2] = piecePlacement

        elif selection == '7' and (row3[0] != 'x' and row3[0] != 'o'):
            row3[0] = piecePlacement

        elif selection == '8'and (row3[1] != 'x' and row3[1] != 'o'):
            row3[1] = piecePlacement

        elif selection == '9' and (row3[2] != 'x' and row3[2] != 'o'):
            row3[2] = piecePlacement
            
        else:
            turnCount = turnCount - 1
            print("\n")
            continue
        #end if


    
    #Check input to play again
        
    while playAgainValid == False:

        playAgainAns = input("Play again? (Y/N): ")

        if playAgainAns == 'Y' or playAgainAns == 'y':
            play = True
            playAgainValid = True
        elif playAgainAns == 'N' or playAgainAns == 'n':
            play = False
            playAgainValid = True
            break
        else:
            if playAgainAns != 'Y' or playAgainAns != 'y' or playAgainAns != 'N' or playAgainAns != 'n':
                playAgainValid = False
                print("Invalid answer\n")
                continue
                

        #end if

print("Thanks for playing!")





