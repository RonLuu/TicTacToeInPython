from game_window import *
from game_logic import *
class TicTacToe:
    def __init__(self):
        print("In tic tac toe class")
        # Create the window of the game
        # self.window = GameWindow()
        # TODO create the game logic
        self.logic = GameLogic()
        # TODO create the game engine

        pass

    def start(self):
        self.logic.begin()

