SIZE = 3
class GameLogic:
    def __init__(self):
        self.state = True # The game begins
        self.turn = True # True for the player 1, False for bot/player 2
        self.board = self.initialiseBoard()
        self.numOfMove = 0
        self.printBoard()
        
        pass
    
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

    def begin(self):
        while(self.state):
            # Check whose turn it is
            self.curChar = "X" if self.turn else "O"
            self.turn = (not self.turn) if self.turn else (not self.turn)
            
            # Get the input from the current player
            position = tuple(input("Enter elements separated by spaces: ").split())
            # TODO check if that's spot taken
            if self.board[int(position[0])][int(position[1])] == '-':
                self.board[int(position[0])][int(position[1])] = self.curChar
            else: 

                self.turn = (not self.turn) if self.turn else (not self.turn)
                print("Choose again")
                continue
            self.printBoard()

            # Check if the game finish
            self.checkFinish()

        if self.curChar == "-":
            print("It's a draw")
        else:
            print(f"{self.curChar} wins")
        
    def checkFinish(self):
        self.numOfMove += 1

        # Check every row in the board
        for i in range(SIZE):
            # if the check row is true
            if self.checkRow(i):
                self.state = False
                return

        # Check every columns in the board
        for j in range(SIZE):
            # if the check row is true
            if self.checkCol(j):
                self.state = False
                return

        if self.checkDiag1():
            self.state = False
            return

        if self.checkDiag2():
            self.state = False
            return

        if self.numOfMove == 9:
            self.curChar = '-'
            self.state = False
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