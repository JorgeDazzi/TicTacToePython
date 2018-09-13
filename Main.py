import sys
from settings.settings import *
from gameEngine import *
from dialogs.console import *

if __name__ == '__main__':
    s = Settings()

    core = TicTacToe(s)

    ui = Console(s, core)


sys.exit(0)




