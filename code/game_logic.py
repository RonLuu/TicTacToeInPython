from game_window import *
SIZE = 3
WIN = 0
LOSE = 1
DRAW = 2
ILLEGAL = 3
CONTINUE = 4
# A class to check the state game (Checking who's winning)
class GameLogic:
    def __init__(self):
        self.board = self.initialiseBoard()
        self.numOfMove = 0
        self.printBoard()
        # A list of what can happen after a move
        self.possible_outcomes = ["win", "lose", "draw", "illegal", "continue"]
        self.state = self.possible_outcomes[CONTINUE] # The game begins
    
    def initialiseBoard(self):
        self.board = []
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                row.append("-")
            self.board.append(row)
        return self.board

    # Helper function
    def printBoard(self):
        for i in range(SIZE):
            for j in range(SIZE):
                print(f"{self.board[i][j]}, ", end = "")
            print()

    def move(self, curChar, curMove):
        x = curMove[0]
        y = curMove[1]

        # If the current position is empty
        if self.board[x][y] == '-':
            self.board[x][y] = curChar
        else: 
            return self.possible_outcomes[ILLEGAL]

        # Check if the game finish
        self.checkFinish(curChar)

        if self.state != self.possible_outcomes[CONTINUE]:
            return self.state

        return self.possible_outcomes[CONTINUE]

    def checkFinish(self, curChar):
        self.numOfMove += 1

        # Check every row in the board
        for i in range(SIZE):
            # if the check row is true
            if self.checkRow(i):
                self.state = self.possible_outcomes[WIN] if curChar == "X" else self.possible_outcomes[LOSE]
                return

        # Check every columns in the board
        for j in range(SIZE):
            # if the check row is true
            if self.checkCol(j):
                self.state = self.possible_outcomes[WIN] if curChar == "X" else self.possible_outcomes[LOSE]
                return

        if self.checkDiag1():
            self.state = self.possible_outcomes[WIN] if curChar == "X" else self.possible_outcomes[LOSE]
            return

        if self.checkDiag2():
            self.state = self.possible_outcomes[WIN] if curChar == "X" else self.possible_outcomes[LOSE]
            return

        if self.numOfMove == 9:
            # The final move leads to a draw
            # No one wins
            self.state = self.possible_outcomes[DRAW]
            return

    # Return true if the row shares the same shape
    def checkRow(self, i):
        for j in range(SIZE-1):
            if self.board[i][j] == '-':
                return False
            if self.board[i][j] != self.board[i][j+1]:
                return False
        return True
    
    # Return true if the col shares the same shape
    def checkCol(self, j):
        for i in range(SIZE-1):
            if self.board[i][j] == '-':
                return False
            if self.board[i][j] != self.board[i+1][j]:
                return False
        return True
    
    # Return true if the diag1 shares the same shape
    def checkDiag1(self):
        return self.board[0][0] != '-' and self.board[0][0] == self.board[1][1] == self.board[2][2] 

    # Return true if the diag2 shares the same shape
    def checkDiag2(self):
        return self.board[0][2] != '-' and self.board[0][2] == self.board[1][1] == self.board[2][0]