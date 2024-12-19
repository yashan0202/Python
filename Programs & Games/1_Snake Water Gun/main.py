'''
We generally prfer numbers while building a game as it is easier to compare numbers than strings,
and for calculation and logic building

1 for Snake
-1 for Water
0 for Gun
'''
import random

computer = random.choice([-1, 0, 1])
player = input("Enter your choice: ")

playerDict = {"s": 1, "w": -1, "g": 0}
playerNum = playerDict[player]

if (computer == playerNum):
    print("It's a tie!")

else:
    if (computer==-1 and playerNum==1):
        print("Computer chose Water. You chose Snake. You win by drinking the water!")

    elif (computer==-1 and playerNum==0):
        print("Computer chose Water. You chose Gun. Computer wins! as Gun drowned in water.")

    elif (computer==1 and playerNum==0):
        print("Computer chose Snake. You chose Gun. You win by shooting the Snake!")

    elif (computer==1 and playerNum==-1):
        print("Computer chose Snake. You chose Water. Computer win by drinking the water!")

    elif (computer==0 and playerNum==1):
        print("Computer chose Gun. You chose Snake. Computer wins by shooting the Snake!")

    elif (computer==0 and playerNum==-1):
        print("Computer chose Gun. You chose Water. You win! as Gun drowned in water!")

    else:
        print("It's a tie!")