class Player:

    __id = None
    __name = None
    __stamp = None


    def __init__(self, id, name, stamp):
        self.__id = id
        self.__name = name
        self.__stamp = stamp

    def getId(self):
        return self.__id

    def getStamp(self):
        return self.__stamp

    def getName(self):
        return self.__name