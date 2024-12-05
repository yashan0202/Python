class Remote():
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

    def moveBottom(self):
        pass

button1 = Remote()
player1 = Player()

if (button1.isLeftPressed()):
    player1.moveLeft()