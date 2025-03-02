from game_window import *
from game_logic import *
class TicTacToe:
    def __init__(self):
        print("In tic tac toe class")
        # Create the logic of the game
        self.logic = GameLogic()
        # Create the window of the game
        self.window = GameWindow(self.logic)
        # TODO create the game engine

        pass

