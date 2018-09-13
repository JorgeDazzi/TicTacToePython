from random import randint
from player import Player
from bot.ai import Bot


class TicTacToe:

    __battlefield = []
    __players = []
    __turn = []
    __ui = None
    __config = None

    def __init__(self, settings):
        self.__config = settings
        self.initBattlefield()

    def initTurn(self):
        self.__turn.append(self.getRandomPlayerId())

    def getBattlefieldSize(self):
        return len(self.__battlefield)

    def getBattleField(self):
        return self.__battlefield

    def addPlayer(self, id, name):
        player = Player(id, name, self.__config.PLAYER_SIGN[id])
        self.__players.append(player)

    def addBot(self):
        bot = Bot(2, self.__config.PLAYER_SIGN[2], self.__config, self.__battlefield)
        self.__players.append(bot)

    def setNextTurn(self):
        current = self.getCurrentPlayer().getId()
        current = current+1 if current+1 < 3 else 0
        self.__turn.append(current)

    def getCurrentPlayer(self):
        return self.__players[self.__turn[-1]]


    def initBattlefield(self):
        """
        Initializing the board game, in this case, battlefield :)
        """
        for x in range(self.__config.BATTLEFIELD):
            row = []
            for y in range(self.__config.BATTLEFIELD):
                row.append(self.__config.EMPTY)
            self.__battlefield.append(row)

    def getRandomPlayerId(self):
        if len(self.__players) > 0:
            return randint(0, len(self.__players)-1)
        return -1

    def setPlot(self, plot):
        self.__battlefield[int(plot[0])][int(plot[2])] = self.getCurrentPlayer().getStamp()

    def printBattlefield(self):
        x = 0
        y = 0
        line = "   "

        #columns headers
        for num in range(len(self.__battlefield)):
            line += " " + str(num)
            if num < len(self.__battlefield)-1:
                line += " ."

        print(line)

        #print Battlefield
        for r in self.__battlefield: #rows
            x = 0
            line = str(x) + " ."

            for c in r: #cols
                line += " " + c + " "

                if x < len(self.__battlefield)-1:
                    line += "|"

                x += 1

            y += 1

            print(line)

            if y < len(self.__battlefield):
                line = "   "
                line += "---+" * (len(self.__battlefield) - 1)
                line += "-" * 3
                print(line)





