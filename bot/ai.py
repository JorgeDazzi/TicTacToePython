from random import randint
from player import Player


class Bot(Player):

    __hist = []
    __config = None
    __battlefield = None

    def __init__(self, id, stamp, config, board):
        Player.__init__(self, id, 'AI', stamp)
        self.__config = config
        self.__battlefield = board

    def getCoordValidation(self, x, y):
        if self.__battlefield[x][y] == self.__config.EMPTY:
            return True
        else:
            return False

    def getHistValidation(self, x, y):
        if len(self.__hist) > 0:

            for coord in self.__hist:
                if coord['x'] == x and coord['y'] == y:
                    return False

        return True

    def getBotMove(self):
        for x in range(len(self.__battlefield)):
            for y in range(len(self.__battlefield[x])):
                if self.__battlefield[x][y] is not self.__config.EMPTY and self.__battlefield[x][y] is not self.getStamp():
                    if self.getHistValidation(x, y):
                        self.__hist.append({
                            'x': x,
                            'y': y
                        })
                        return self.getDefensePostion(x, y)

        return "0,0"

    def getDefensePostion(self, x, y):
        addX = randint(0, 2)
        addY = randint(0, 2)

        x += addX
        y += addY
        x = x if x < len(self.__battlefield) else 0
        y = y if y < len(self.__battlefield) else 0

        if self.getCoordValidation(x, y):
            return "%s,%s" % (x, y)
        else:
            return self.getDefensePostion(x, y)


