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

# To win you would need 000, 111 , 222, 012 - with 
# sorted from least to greatest
def checkBoard(row0, row1, row2, player):
    
    xArray = []
    yArray = []
    checkArray = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
    for (index, row) in enumerate(row0):
    
        if player == 'X':
            
            if row0[index] == 'X':
              value = index + 1
              xArray.append(value)
              xArray.sort()

            if row1[index] == 'X':
             value = index + 4
             xArray.append(value)
             xArray.sort()

            if row2[index] == 'X':
             value = index + 7
             xArray.append(value)
             xArray.sort()
             
        else: 
            
            if row0[index] == 'O':
             value = index + 1
             yArray.append(value)
             yArray.sort()
             
            if row1[index] == 'O':
             value = index + 4
             yArray.append(value)
             yArray.sort()

            if row2[index] == 'O':
             value = index + 7
             yArray.append(value)
             yArray.sort()
                
    
    for checkArr in checkArray:
        if all(x in xArray for x in checkArr):
            print("X's won !")
            return True

        if all(y in yArray for y in checkArr):
            print("Y's won !")
            return True

    return False
    
   
        
    

def playTTT():
    print("Welcome to Command Line Tic Tac Toe")
    player1Turn = True
    winner = False
    row0 = [" "," "," "]
    row1 = [" "," "," "]
    row2 = [" "," "," "]

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
                 winner = checkBoard(row0, row1, row2, 'X')
                 player1Turn = False
                else:
                 player1Turn = True

           elif rowNumber == '1':
                select = boardSelection(row1, positionNumber, player1)

                if select is not False:
                 row1 = select
                 winner = checkBoard(row0, row1, row2, 'X')
                 player1Turn = False
                else:
                 player1Turn = True
                   
           elif rowNumber == '2':
                select = boardSelection(row2, positionNumber, player1)

                if select is not False:
                 row2= select
                 winner = checkBoard(row0, row1, row2, 'X')
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
                winner = checkBoard(row0, row1, row2, 'O')
                player1Turn = True
             else:
                player1Turn = False

            elif rowNumber == '1':
             select = boardSelection(row1, positionNumber, player2)

             if select is not False:
                row1 = select
                winner = checkBoard(row0, row1, row2, 'O')
                player1Turn = True
             else:
                player1Turn = False
                   
            elif rowNumber == '2':
             select = boardSelection(row2, positionNumber, player2)

             if select is not False:
                row2 = select
                winner = checkBoard(row0, row1, row2, 'O')
                player1Turn = True
             else:
                player1Turn = False
                
            

            

    
    


playTTT()