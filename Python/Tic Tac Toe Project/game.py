# 2 Players should be able to play the game sitting at the same computer
# The board she be printed every time with the updated positions

player1 = ""
player2 = ""

# board = {
#     print("1", "2", "3"),
#     print("4", "5", "6"),
#     print("7", "8", "9 ")
# }


def playerSelection():

    player1Selection = "game"

    while player1Selection.lower() not in ["x", "o"]:

        player1Selection = input("Player 1 do you want to be X or O's ?")

        if player1Selection.lower() not in ["x", "o"]:
            print("This is not a valid selection")
        else:
            pass


    if player1Selection.lower() == "x":
        player1 = "x"
        player2 = "o"
        print("Player 1 you are X's and Players 2 you are O's")
        return
        
    else:
        player1 = "o"
        player2 = "x"
        print("Player 1 you are O's and Players 2 you are X's")
        return

playerSelection()


print("Player 1 " + player1)