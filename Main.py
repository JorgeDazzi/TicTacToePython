import sys
from settings.settings import *
from gameEngine import *
from dialogs.console import *




s = Settings()

core = TicTacToe(s)

ui = Console(s, core)




sys.exit(0)




