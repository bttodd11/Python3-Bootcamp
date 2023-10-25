# 2 Players should be able to play the game sitting at the same computer
# The board she be printed every time with the updated positions

# Steps
#1. Show blank board- DONE
#2. Ask Player one to select the positions - DONE
#3. Make a selection for Row and Positions - DONE
#4. From that selection mark an x or o on the board and return the board - DONE
#5. Repeat step 3 and 4 until there is a win
#6 Check to see if there is a winner after step 4

def createBoard(row0,row1,row2):
    print(row0)
    print(row1)
    print(row2)


def playerSelection():
    player1Selection = "game"

    while player1Selection.upper() not in ["X", "O"]:

        player1Selection = input("Player 1 do you want to be X or O's ?").upper()

        if player1Selection.upper() not in ["X", "O"]:
            print("This is not a valid selection")
        else:
            pass


    if player1Selection.upper() == "X":
        print("Player 1 you are X's and Players 2 you are O's")
        return ["X", "O"]        
    else:
        print("Player 1 you are O's and Players 2 you are X's")
        return ["O", "X"]


def playerMove(player):
    row = 10
    position = 10

    while row not in ["0","1","2"]:

        row = input(player + " select a row (0 - 2) : ")
        if row.isnumeric() != True or int(row) not in [0,1,2]:
            print("This is not a valid selection")

    while position not in ["0","1","2"]:

        position = input(player + " select a position (0 - 2) : ")
        if position.isnumeric() != True or int(position) not in [0,1,2]:
            print("This is not a valid selection")

    return [row,int(position)]

def boardSelection(row, selection, player):
    while row[selection].upper() == 'X' or row[selection].upper() == 'O':
        print("This position has been taken")
        return False


    row[selection] = player
    return row


def playTTT():
    print("Welcome to Command Line Tic Tac Toe")
    player1Turn = True
    winner = False
    row0 = ["","",""]
    row1 = ["","",""]
    row2 = ["","",""]

    selection = playerSelection()
    player1 = selection[0]
    player2 = selection[1]


    while winner == False:

        createBoard(row0, row1, row2)

        if player1Turn == True:
           playerChoices = playerMove(player1)
           rowNumber = playerChoices[0]
           positionNumber = playerChoices[1]


           if rowNumber == '0':
             select = boardSelection(row0, positionNumber, player1)

             if select is not False:
                row0 = select
                player1Turn = False
             else:
                player1Turn = True

           elif rowNumber == '1':
                select = boardSelection(row1, positionNumber, player1)

                if select is not False:
                    row1 = select
                    player1Turn = False
                else:
                    player1Turn = True
                   
           elif rowNumber == '2':
                select = boardSelection(row2, positionNumber, player1)

                if select is not False:
                    row1 = select
                    player1Turn = False
                else:
                    player1Turn = True
        
        else: 
            playerChoices = playerMove(player2)
            rowNumber = playerChoices[0]
            positionNumber = playerChoices[1]

            if rowNumber == '0':
             select = boardSelection(row0, positionNumber, player2)

             if select is not False:
                row0 = select
                player1Turn = True
             else:
                player1Turn = False

            elif rowNumber == '1':
             select = boardSelection(row1, positionNumber, player2)

             if select is not False:
                row1 = select
                player1Turn = True
             else:
                player1Turn = False
                   
            elif rowNumber == '2':
             select = boardSelection(row2, positionNumber, player2)

             if select is not False:
                row2 = select
                player1Turn = True
             else:
                player1Turn = False

            

    
    


playTTT()