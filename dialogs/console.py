#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from dialogs.msgs import *


class Console:

    __config = None
    __size = 0
    __core = None

    def __init__(self, config, core):
        self.__config = config
        self.__size = core.getBattlefieldSize()
        self.__core = core

        #Welcome
        self.getGreetings()
        self.initGameSession()

    def getGreetings(self):
        print(Msgs.UI.get("welcome").get(self.__config.LANGUAGE));

    def getPlayerName(self, id):
        while True:
            print("Player %s => %s [ %s ]" % (
                      id,
                      Msgs.UI.get("playerName").get(self.__config.LANGUAGE),
                      Msgs.UI.get("playerSizeChars").get(self.__config.LANGUAGE)
                  ))

            name = input()

            #check name
            if len(name.strip()) >= 2:
                print(Msgs.UI.get("playerSet").get(self.__config.LANGUAGE) % id)
                print()#Margin bottom ;)

                return name

            else:
                print(Msgs.WARMING.get("playerSetWrong").get(self.__config.LANGUAGE))

    def getWinnerAnnounce(self, name, id):
        print(Msgs.UI.get("winnerAnnounce").get(self.__config.LANGUAGE) % (name, id))
        sys.exit(0)

    def getMoveValidation(self):
        max = self.__size -1

    def getCoordValidation(self, x, y):
        print(self.__config.EMPTY)
        if self.__core.getBattleField()[x][y] == self.__config.EMPTY:
            return True
        else:
            return False


    def getPlayerMove(self, player):

        while True:
            print("")
            print(Msgs.UI.get("moveInstruction").get(self.__config.LANGUAGE) % (self.__size-1))
            print(Msgs.UI.get("move").get(self.__config.LANGUAGE) % (player.getName(), player.getId()))

            if player.getId() is not 2:
                move = input()

                if bool(re.match('^[0-%s],[0-%s]$' % (self.__size-1, self.__size-1), move)):
                    if self.getCoordValidation(int(move[0]), int(move[2])):
                        return move
                    else:
                        print(Msgs.WARMING.get("coordUsed").get(self.__config.LANGUAGE) % move)

                else:
                    print(Msgs.WARMING.get("wrongMove").get(self.__config.LANGUAGE) % move)
            else:
                move = player.getBotMove()
                print(move)
                return move


    def initGameSession(self):

        #Player 1
        pname = self.getPlayerName(0)
        self.__core.addPlayer(0, pname)

        #Player 2
        pname = self.getPlayerName(1)
        self.__core.addPlayer(1, pname)

        #Bot
        self.__core.addBot()

        #Shuffle who play first
        self.__core.initTurn()

        self.__core.printBattlefield() #display the board first time

        while True:

            player = self.__core.getCurrentPlayer()

            if player.getId() == 2:
                move = self.getPlayerMove(player)
            else:
                move = self.getPlayerMove(player)

            #Plot
            winner = self.__core.setPlot(move)

            #Print Board
            self.__core.printBattlefield()

            if winner == 9:
                print(Msgs.UI.get("announceTheWinner").get(self.__config.LANGUAGE) % (player.getName(), player.getId()))
                sys.exit(0)
            elif winner == 1:
                print(Msgs.UI.get("drawGame").get(self.__config.LANGUAGE))
                sys.exit(0)

            #Set next Turn
            self.__core.setNextTurn()



