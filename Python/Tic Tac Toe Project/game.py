# 2 Players should be able to play the game sitting at the same computer
# The board she be printed every time with the updated positions

# Steps
#1. Show blank board- DONE
#2. Ask Player one to select the positions - DONE
#3. Make a selection for Row and Positions - DONE
#4. From that selection mark an x or o on the board and return the board
#5. Repeat step 3 and 4 until there is a win
#6 Check to see if there is a winner after step 4


row1 = ["","","x"]
row2 = ["","",""]
row3 = ["","",""]


def createBoard(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


def playerSelection():
    player1Selection = "game"

    while player1Selection.lower() not in ["x", "o"]:

        player1Selection = input("Player 1 do you want to be X or O's ?")

        if player1Selection.lower() not in ["x", "o"]:
            print("This is not a valid selection")
        else:
            pass


    if player1Selection.lower() == "x":
        print("Player 1 you are X's and Players 2 you are O's")
        return ["x", "o"]        
    else:
        print("Player 1 you are O's and Players 2 you are X's")
        return ["o", "x"]


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

    return [row,position]

def boardSelection(row, selection, player):

    while row[selection] :
        print("This position has been taken")
        playerMove(player)

    row[selection] = player
    return row




# order = playerSelection()

# createBoard(row1,row2,row3)
# playerMove("X")

row1 = boardSelection(row1, 2, "x")

print(row1)