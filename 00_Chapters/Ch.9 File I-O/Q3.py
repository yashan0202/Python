'''The game() function in a program lets a user play a game and returns the
   score as an interger. You need to raed a file 'Hi-score.txt' which is either
   blank or contains the previous high score. You need to write a program to
   update the file with the high score whenever game() breaks the high score.'''

import random

def game():
    print("You are playing a game...")
    score = random.randint(1, 100)
    # fetch the highscore
    with open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\Q3_highscore.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your score is {score}")
    if (score>highscore):
        # write this highscore to the file
        with open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\Q3_highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()