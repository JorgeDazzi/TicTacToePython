from dialogs.msgs import *


class Settings:

    LANGUAGE = 'EN'

    BATTLEFIELD = 3

    PLAYER_SIGN = [
        u"\u2716",
        u"\u25CF",
        u"\u25BC"
    ]

    EMPTY = " "

    __settings = {}

    def __init__(self):
        self.getConfigFile()
        self.getBattlefieldSize()
        self.getPlayerSign(0) #player 1
        self.getPlayerSign(1) #player 2
        self.getPlayerSign(2) #player AI
        self.getLanguage()

    def getConfigFile(self):
        """
        Reading and set __settings for retrieve settings form config file, in order to replace the DEFAULT values
        """
        configFile = open("config", "r")

        for line in configFile:
            config = line.split(":")

            if len(config) == 2:
                self.__settings[config[0]] = config[1].replace("\n", "")

    def getIsNotDuplicated(self, value):
        """
        Prevent players from having the same signs/stamps.

        :param value: sign that you want check if is not duplicated
        :return: True = no Duplicated | False = Duplicated
        """

        for sign in self.PLAYER_SIGN:
            if sign == value:
                return False

        # no duplicated sign found
        return True

    def getLanguage(self):
        """
        Loading the LANGUAGE from Config file
        """

        value = self.__settings.get("language")

        if value is not None:
            try:
                if value.strip() is not "":
                    self.LANGUAGE = value.strip()

            except:
                print(Msgs.ERROR.get("inputTypeIsWrong").get(self.LANGUAGE))

    def getBattlefieldSize(self):
        """
        Loading the BATTLEFIELD_SIZE from config file
        """

        size = self.__settings.get("battlefieldSize")

        if size is not None:
            try:
                size = int(size)
                if 3 <= size <= 10:
                    self.BATTLEFIELD = size
            except:
                print(Msgs.ERROR.get("inputTypeIsWrong").get(self.LANGUAGE))

    def getPlayerSign(self, id):
        """
        Loading the BATTLEFIELD_SIZE from config file
        """

        options = {
            0 : "playerOneSymbol",
            1 : "playerTwoSymbol",
            2 : "playerAiSymbol"
        }

        player = options.get(id)

        sign = self.__settings.get(player)

        if sign is not None:
            try:

                if len(sign.strip()) == 1 and sign.strip() is not "":
                    self.PLAYER_SIGN[id] = sign

                else:
                    print(player+" :: "+Msgs.ERROR.get("playerValue").get(self.LANGUAGE))

            except:
                print(Msgs.ERROR.get("inputTypeIsWrong").get(self.LANGUAGE))






